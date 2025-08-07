import pandas as pd


def main():
    meta_df = pd.read_csv("data/MBSpeech-1.0/metadata_unprep.csv", sep="|", header=None)
    file_names = meta_df.iloc[:, 0]
    relative_path_to_wavs = [f"wavs/{file_name}.wav" for file_name in file_names]
    meta_df.iloc[:, 0] = relative_path_to_wavs
    meta_df.to_csv("data/MBSpeech-1.0/metadata.csv", sep="|", header=False, index=False)
    print("Metadata preparation completed. Check data/MBSpeech-1.0/metadata.csv for the updated file.") 



if __name__ == "__main__":
    main()
