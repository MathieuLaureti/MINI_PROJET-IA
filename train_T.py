import os

# Define paths for your training files (no need to provide full paths)
output_dir = "training_data"
font_properties_file = "font_properties"
unicharset_file = "unicharset"
output_trainer_file = "output_trainer"

# Example to run `mftraining` command (without full path)
mftraining_command = f'mftraining -F "{font_properties_file}" -U "{unicharset_file}" -O "{output_trainer_file}" -D "{output_dir}"'

# Example to run `cntraining` command (without full path)
cntraining_command = f'cntraining "{output_dir}"'

# Example to run `combine_tessdata` command (without full path)
combine_tessdata_command = f'combine_tessdata "{output_trainer_file}"'

# Run the commands using os.system
def run_command(command):
    print(f"Running command: {command}")
    result = os.system(command)  # This will execute the command in the command prompt
    if result == 0:
        print("Command executed successfully!")
    else:
        print(f"Command failed with error code {result}")

# Run MFTraining
run_command(mftraining_command)

# Run CNTraining
run_command(cntraining_command)

# Run Combine_Tessdata
run_command(combine_tessdata_command)
