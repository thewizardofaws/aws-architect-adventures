# AWS Architect Adventures

Welcome to the repository for **AWS Architect Adventures**! This project is designed to grow my personal brand as an AWS evangelist, featuring a blog, podcast, and more. The website is hosted on AWS as a serverless static website.

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

**AWS Architect Adventures** is a personal website that includes:

- **Home Page**: An overview of the latest blog posts and podcast episodes.
- **Podcast Page**: A list of podcast episodes with descriptions and links.
- **Blog Page**: A collection of blog posts with summaries and links.
- **AWS Utah Page**: Information about the AWS Utah user group.
- **Resume Page**: My professional resume and career highlights.

The website is designed to be fully serverless, leveraging various AWS services for hosting, content delivery, and more.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: AWS Lambda (for content processing)
- **Hosting**: Amazon S3, Amazon CloudFront
- **CI/CD**: AWS Amplify, AWS CodePipeline, AWS CodeBuild
- **Others**: AWS Route 53 (DNS), AWS Certificate Manager (SSL/TLS)

## Folder Structure

awsarchitectadventures/
│
├── src/
│ ├── assets/
│ │ ├── images/
│ │ ├── css/
│ │ │ └── styles.css
│ │ ├── js/
│ │ │ └── scripts.js
│ │ └── fonts/
│ ├── content/
│ │ ├── blog/
│ │ ├── podcast/
│ │ └── aws-utah/
│ ├── templates/
│ │ ├── partials/
│ │ │ ├── header.html
│ │ │ ├── footer.html
│ │ │ └── nav.html
│ │ ├── index.html
│ │ ├── blog.html
│ │ ├── podcast.html
│ │ ├── aws-utah.html
│ │ └── resume.html
│ └── scripts/
│ └── markdown_to_html.py
│
├── build/
│ ├── assets/
│ │ ├── images/
│ │ ├── css/
│ │ │ └── styles.css
│ │ ├── js/
│ │ │ └── scripts.js
│ │ └── fonts/
│ ├── blog/
│ │ └── index.html
│ ├── podcast/
│ │ └── index.html
│ ├── aws-utah/
│ │ └── index.html
│ ├── index.html
│ ├── blog.html
│ ├── podcast.html
│ ├── aws-utah.html
│ └── resume.html
│
├── amplify/
│ ├── .config/
│ ├── backend/
│ ├── team-provider-info.json
│
├── .gitignore
├── amplify.yml
├── package.json
├── README.md


## Getting Started

### Prerequisites

- Node.js and npm installed
- AWS CLI installed and configured
- Amplify CLI installed and configured

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/awsarchitectadventures.git
    cd awsarchitectadventures
    ```

2. **Install dependencies**:

    ```sh
    npm install
    ```

3. **Initialize Amplify**:

    ```sh
    amplify init
    ```

4. **Add hosting**:

    ```sh
    amplify add hosting
    amplify publish
    ```

## Deployment

### Build Process

1. **Build the project**:

    Use a build tool to process the source files in `src/` and output the final files into the `build/` directory.

    Example using a custom script:

    ```sh
    npm run build
    ```

2. **Deploy to S3**:

    Use the AWS CLI to sync the contents of the `build/` directory to the S3 bucket.

    ```sh
    aws s3 sync build/ s3://awsarchitectadventures.com/ --delete
    ```

3. **Invalidate CloudFront Cache**:

    Invalidate the CloudFront cache to ensure the latest changes are reflected.

    ```sh
    aws cloudfront create-invalidation --distribution-id YOUR_DISTRIBUTION_ID --paths "/*"
    ```

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

