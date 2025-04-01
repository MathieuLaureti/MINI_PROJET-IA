import subprocess
import os

def extract_and_merge_traineddata(file1, file2, output_dir):
    # Extract base names (without extensions) of the two files
    base_name1 = os.path.splitext(file1)[0]
    base_name2 = os.path.splitext(file2)[0]
    
    # Create the new output file name (concatenate both names with a "+" in the middle)
    output_file = f"{base_name1}+{base_name2}.traineddata"
    output_path = os.path.join(output_dir, output_file)
    
    # Full paths for the original files
    file1_path = os.path.abspath(file1)
    file2_path = os.path.abspath(file2)
    
    # Extract base names (without path) for combine_tessdata
    base_name1 = os.path.basename(base_name1)
    base_name2 = os.path.basename(base_name2)
    
    # Ensure that file paths are correctly formatted (not needed if absolute paths are correct)
    file1_path = file1_path.replace("\\", "/")
    file2_path = file2_path.replace("\\", "/")

    print("test",file1_path,file2_path)
    
    # Step 1: Extract components from both traineddata files
    try:
        # Extract components of the first traineddata
        extract_command1 = f"combine_tessdata -e {file1_path}"
        subprocess.run(extract_command1, shell=True, check=True)

        # Extract components of the second traineddata
        extract_command2 = f"combine_tessdata -e {file2_path}"
        subprocess.run(extract_command2, shell=True, check=True)

        # Now that the components are extracted, combine them
        # Step 2: Combine the extracted components into a new traineddata
        combine_command = f"combine_tessdata {base_name1}+{base_name2}."
        subprocess.run(combine_command, shell=True, check=True)

        # Step 3: Move the combined traineddata to the output directory
        if os.path.exists(f"{base_name1}+{base_name2}.traineddata"):
            os.rename(f"{base_name1}+{base_name2}.traineddata", output_path)
            print(f"Successfully merged {file1} and {file2} into {output_file}")
            print(f"Output saved as: {output_path}")
        else:
            print(f"Error: Combined traineddata file was not created.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running command: {e.cmd}")
        print(f"Error message: {e.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
extract_and_merge_traineddata('Dancing_500.traineddata', 'eng.traineddata', 'C:/Users/mathi/OneDrive/Documents/GitHub/MINI_PROJET-IA/trained_data/')
