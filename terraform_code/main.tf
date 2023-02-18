provider "aws" {
  #access_key="AKIAZ7UXADKMV2UMJXFN"
  #secret_key="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"
  region = "us-east-1"
}
resource "aws_instance" "vm" {
  ami           = "ami-0fe472d8a85bc7b0e"
  subnet_id     = "subnet-0e41e709312ae01bd"
  instance_type = "t3.micro"
  tags = {
    Name = "my-first-tf-node"
  }
}
