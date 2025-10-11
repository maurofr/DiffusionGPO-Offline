from huggingface_hub import upload_file

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--hf_token', type=str, required=True, help="Hugging Face token for authentication")
    parser.add_argument('--local_path', type=str, required=True, help="Path to local unet checkpoint")
    parser.add_argument('--repo_id', type=str, required=True, help="Huggingface repo ID")
    return parser.parse_args()

def main():
    args = parse_args()

    for fname in ['config.json', 'diffusion_pytorch_model.safetensors']:
        print(f"Uploading {fname}...")
        upload_file(path_or_fileobj= args.local_path + fname,
                    path_in_repo=fname,
                    repo_id = args.repo_id, 
                    token=args.hf_token 
                )
        
if __name__ == "__main__":
    main()
