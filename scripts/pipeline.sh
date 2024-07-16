set -e

aws cloudformation deploy \
  --template-file ci/codepipeline.yml \
  --stack-name codepipeline-vatsim-data-api-proxy \
  --capabilities CAPABILITY_IAM \
  --region eu-west-1 \
  --profile vatsim-data
