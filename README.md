# Jareth

Jareth is a simple chatbot which runs in AWS lambda and responds to Twilio webhooks.
Once installed and configured, it will respond to SMS messages on the Twilio number and only understands the classic, "You remind me of the babe" song from the movie Labrynth.
https://youtu.be/FfccgkG6Og8

To get started, set everything up then text "you remind me of the babe" to Jareth's phone number to begin your conversation.

This document doesn't describe how to setup and configure either Lambda or Twilio.  You're on your own for that.

## Requirements:
  * Docker (for development and building)
  * AWS account with a new Lambda function
  * Twilio account with SMS number

## Running:
  * Upload your jareth.zip file to Lambda
  * Create a new layer and upload the layer.zip to it
  * Set the following environment variables and add the relevant info:
    | Variable           | Description                                  |
    |--------------------|----------------------------------------------|
    | TWILIO_ACCOUNT_SID | your account SID                             |
    | TWILIO_AUTH_TOKEN  | your auth token                              |
    | TWILIO_NUMBER      |your new phone number (configured to use SMS) |
  * Create a new API gateway and use the URL for the Twilio endpoint.
  * Do all the other stuff I neglected to mention here.

## Makefile commands:
* ```make all```
  Clean and make everything.
* ```make layer```
  Create the AWS lambda layer.zip file containing the package dependencies.
* ```make lambda```
  Create the lambda.zip file which you can upload to your lambda function.
* ```make clean```
  Clean the project files.
 
