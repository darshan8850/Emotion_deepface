import readline from 'readline';
import { oraPromise } from 'ora';
import { BingChat } from './src';
import dotenv from 'dotenv-safe';
import { exec } from 'child_process';

dotenv.config();

async function chatbot() {
  const api = new BingChat({ cookie: process.env.BING_COOKIE });
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  let emotion = await new Promise<string>((resolve) => {
    exec('python emotion_detection.py', (error, stdout, stderr) => {
      if (error) {
        console.log(`error: ${error.message}`);
        resolve('neutral'); // default to neutral emotion
      } else if (stderr) {
        console.log(`stderr: ${stderr}`);
        resolve('neutral'); // default to neutral emotion
      } else {
        resolve(stdout.trim());
      }
    });
  });
  const input = await new Promise<string>((resolve) => {
    rl.question('Enter your message (or type "exit" to quit): ', (answer) => {
      resolve(answer);
    });
  });
  const response = await oraPromise(api.sendMessage(input), {
    text: input,
  });

  console.log(response.text);

  console.log(`Why are you ${emotion} today?`);

  while (true) {
    const input = await new Promise<string>((resolve) => {
      rl.question('Enter your message (or type "exit" to quit): ', (answer) => {
        resolve(answer);
      });
    });

    if (input.toLowerCase() === 'exit') {
      console.log('Nice chatting with you!');
      break;
    }

    const response = await oraPromise(api.sendMessage(input), {
      text: input,
    });

    console.log(response.text);
  }

  rl.close();
}

chatbot().catch((err) => {
  console.error(err);
  process.exit(1);
});
