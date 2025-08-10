import pandas as pd

raw_file_path = r"C:\Users\45378128\Desktop\Projects_Footprint_Analysis\QS_Project Contacts Latest 10 Aug.xlsx"
cleaned_file_path = r"C:\Users\45378128\Desktop\Projects_Footprint_Analysis\QlikSense_streams_mapping_cleaned.csv"

# Read the Excel file
data_df = pd.read_excel(raw_file_path, sheet_name="Apps-Session-Temp")

output_data = []

for idx, row in data_df.iterrows():
    stream_name = row["Stream"]
    app_name = row["App"]
    sessions = row["Sessions"]
    users = row["Users"]
    session_duration = row["Session Duration"]

    if isinstance(stream_name, str):
        for s in stream_name.split("\n"):
            output_data.append({
                "Stream": s,
                "app_name": app_name,
                "Sessions": sessions,
                "Users": users,
                "session_duration": session_duration
            })
    else:
        output_data.append({
            "Stream": stream_name,
            "app_name": app_name,
            "Sessions": sessions,
            "Users": users,
            "session_duration": session_duration
        })

df_cleaned_output = pd.DataFrame(output_data)

# Drop rows where 'Stream' is null
df_cleaned_output_drop_Null = df_cleaned_output.dropna(subset=["Stream"])

# Clean the 'Stream' column
df_cleaned_output_drop_Null["Cleaned_Streams"] = df_cleaned_output_drop_Null["Stream"].str.upper()
df_cleaned_output_drop_Null["Cleaned_Streams"] = df_cleaned_output_drop_Null["Cleaned_Streams"].str.replace(r"[^A-Z0-9]", "", regex=True)

# Save to CSV
df_cleaned_output_drop_Null.to_csv(cleaned_file_path, index=False)
print(f"QS_Project_streams_mapping_cleaned saved to {cleaned_file_path}")
