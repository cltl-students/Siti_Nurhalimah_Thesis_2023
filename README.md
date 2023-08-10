# Description
This repository is a part of the thesis project for MA Linguistics (Human Language Technology). The project focuses on conducting data analysis and implementing an intersection algorithm on the OPUS corpus from https://opus.nlpl.eu/ and the Wiktionary dataset from https://kaikki.org/dictionary/English/index.html. This repository contains tools and scripts for performing sense alignment and evaluation using various datasets and algorithms. The repository is organized into different subfolders and contains a variety of Jupyter notebooks and Python scripts to facilitate the process.

## opus Folder

The `opus` folder contains data related to the OPUS corpus, a parallel data collection. It is organized as follows:

### Subfolders:

- **data**: This folder stores all the files of the original parallel data from SourceForge.
- **predictions_results**: Here, you can find the prediction results of the system's sense alignment.
- **raw_data_bible**: Contains the Bible (Uedin) corpus.
- **raw_data_opensubtitle**: Holds the OpenSubtitles corpus.
- **raw_data_qed**: Contains the QED corpus.
- **raw_data_tanzil**: Stores the Tanzil corpus.

### Jupyter Notebooks:

- **1.opus_extraction.ipynb**: Parses data from the four different corpora.
- **2. intersection_algorithm_opus.ipynb**: Maps senses using the intersection algorithm on the OPUS data.
- **3. opus_algorithm_based_conditions.ipynb**: Runs the mapped senses based on five conditions.
- **4. opus_token_count.ipynb**: Counts the number of tokens in the OPUS corpus for data analysis.
- **5. opus_languages_intersection_analysis.ipynb**: Counts the number of language intersections in the OPUS corpus.
- **6. data_analysis.ipynb**: Counts the number of senses suggested by one or two languages in the development set for data analysis.
- **7. error_analysis.ipynb**: Counts senses suggested by certain languages based on evaluation set results for error analysis.
- **8. evaluation_set.ipynb**: Generates matching between OPUS and the evaluation set and runs the intersection algorithm using the best condition (condition 5).
- **classification_report_generator.py**: Generates a classification report in the `predictions_results` folder.

## wiktionary Folder

The `wiktionary` folder contains data related to the Wiktionary dataset. It is structured as follows:

### Subfolders:

- **data**: This directory stores all the files of the original parallel data from SourceForge.
- **predictions_results**: This is where the prediction results of the system's sense alignment are stored.

### Jupyter Notebooks:

- **1. wiktionary_extraction.ipynb**: Parses data from the Wiktionary JSON file downloaded from [kaikki.org](https://kaikki.org/dictionary/English/index.html).
- **2. intersection_algorithm_wiktionary.ipynb**: Maps senses using the intersection algorithm on the Wiktionary data.
- **3. wiktionary_algorithm_based_conditions.ipynb**: Runs the mapped senses based on five conditions.
- **4. wiktionary_token_count.ipynb**: Counts the number of tokens in the Wiktionary dataset for data analysis.
- **5. wiktionary_languages_intersection_analysis.ipynb**: Counts the number of language intersections in the Wiktionary dataset.
- **6. POS_analysis.ipynb**: Counts the number of parts of speech (POS) in Wiktionary for data analysis.
- **7. data_analysis.ipynb**: Counts the number of senses suggested by one or two languages in the development set for data analysis.
- **8. evaluation_set.ipynb**: Generates matching between Wiktionary and the evaluation set and runs the intersection algorithm using the best condition (condition 5).
- **9. error_analysis.ipynb**: Counts senses suggested by certain languages based on evaluation set results for error analysis.
- **classification_report_generator.py**: Generates a classification report in the `predictions_results` folder.

## wn-msa-all Folder

The `wn-msa-all` folder contains data related to the WordNet Multilingual Synset Alignments (wn-msa) dataset:

### Subfolders:

- **data**: This folder stores all the files of the original parallel data from SourceForge.
- **predictions_results**: Here, you can find the prediction results of the system's sense alignment.

### Jupyter Notebooks:

- **1. development_evaluation_sets.ipynb**: Builds development and evaluation sets.
- **2. goodness_labels_extraction.ipynb**: Extracts data from the main data (https://sourceforge.net/p/wn-msa/tab/HEAD/tree/trunk/) with labels B and I, extracting goodness labels to the development and evaluation sets.
- **3. combined_datasets_on_eval.ipynb**: Combines both Wiktionary and OPUS data and runs the combined dataset on the evaluation set using the best condition. Generates a classification report.
- **4. wn-msa_error_analysis.ipynb**: Suggests senses for the main data (https://sourceforge.net/p/wn-msa/tab/HEAD/tree/trunk/) using Wiktionary and OPUS data respectively for the final error analysis step. Takes 150 random samples from each data source.
- **5. error_analysis_hand-checked.ipynb**: Obtains glosses of the 150 random samples and generates accuracy scores for both Wiktionary and OPUS for the last step of error analysis.
- **senses.ipynb**: This notebook handles sense-related analysis.
- **classification_report_generator.py**: Generates a classification report in the `predictions_results` folder.




# Usage
To use this repository, first clone or download it to your local machine. Then, navigate to the respective folders based on your requirements. Each folder contains notebooks or scripts for specific tasks related to data analysis and intersection algorithms. Follow the instructions provided in the notebooks or scripts to execute the necessary operations.

# Requirements
To run the code in this repository, ensure you have the following installed on your local machine:

- Python 3
- Jupyter Notebook or any Python IDE
- The required Python packages mentioned in the notebooks or scripts

# Contact
If you have any questions or encounter any issues, please feel free to reach out to the project owner at s.nurhalimah@student.vu.nl

# License
Nothing special
