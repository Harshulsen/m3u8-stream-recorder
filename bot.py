
   import os
   import logging
   from telegram import Update
   from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
   import ffmpeg
   import requests

   # Set up logging
   logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

   # Start command
   def start(update: Update, context: CallbackContext) -> None:
       update.message.reply_text('Welcome to M3U8 Stream Recorder! Send me an M3U8 URL.')

   # Function to record stream
   def record_stream(url, quality, duration):
       output_file = f"output_{quality}.mp4"
       command = (
           ffmpeg
           .input(url, t=duration)
           .output(output_file, video_bitrate=quality)
           .run()
       )
       return output_file

   # Handle message
   def handle_message(update: Update, context: CallbackContext) -> None:
       url = update.message.text
       # Here you can add logic to parse quality and duration from user input
       quality = "1000k"  # Example quality
       duration = 10  # Example duration in seconds
       output_file = record_stream(url, quality, duration)
       update.message.reply_text(f"Recording completed! File saved as {output_file}")

   # Main function
   def main() -> None:
       updater = Updater("7001271118:AAHG3GZTRiDY3MxEGxAMYZ16hS4EHzBMHHA")
       dispatcher = updater.dispatcher
       dispatcher.add_handler(CommandHandler("start", start))
       dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
       updater.start_polling()
       updater.idle()

   if __name__ == '__main__':
       main()
   
