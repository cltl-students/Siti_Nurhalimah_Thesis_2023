# Description
This repository is a part of the thesis project for MA Linguistics (Human Language Technology). The project focuses on conducting data analysis and implementing an intersection algorithm on the OPUS corpus from https://opus.nlpl.eu/ and the Wiktionary dataset from https://kaikki.org/dictionary/English/index.html. This repository contains tools and scripts for performing sense alignment and evaluation using various datasets and algorithms. The repository is organized into different subfolders and contains a variety of Jupyter notebooks and Python scripts to facilitate the process.

## Special Note:
Due to limited storage space on GitHub, all the complete repository along with its data can be downloaded from this drive as well:

JSON file for Wiktionary extraction compiled by 

https://kaikki.org/dictionary/English/kaikki.org-dictionary-English.json

## Table of Contents
- [Opus Folder](#opus-folder)
- [Wiktionary Folder](#wiktionary-folder)
- [wn-msa-all Folder](#wn-msa-all-folder)
- [requirement.txt](#requirementtxt)
- [Usage](#usage)
- [Contact](#contact)
- [License](#license)

## opus Folder

The [`opus`](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/opus) folder contains data related to the OPUS corpus, a parallel data collection. It is organized as follows:

### Subfolders:

- [data](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/opus/data) stores all the files of the original parallel data from SourceForge.
- [predictions_results](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/opus/predictions_results) stores prediction results of the system's sense alignment.
- [raw_data_bible](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/opus/raw_data_bible) contains the Bible (Uedin) corpus.
- [raw_data_opensubtitle](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/opus/raw_data_opensubtitle) contains the OpenSubtitles corpus.
- [raw_data_qed](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/opus/raw_data_qed) contains the QED corpus.
- [raw_data_tanzil](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/opus/raw_data_tanzil) stores the Tanzil corpus.

### Jupyter Notebooks:

- [1. opus_extraction.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/opus/1.%20opus_extraction.ipynb) parses data from the four different corpora.
- [2. intersection_algorithm_opus.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/opus/2.%20intersection_algorithm_opus.ipynb) maps senses using the intersection algorithm on the OPUS data.
- [3. opus_algorithm_based_conditions.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/opus/3.%20opus_algorithm_based_conditions.ipynb) runs the mapped senses based on five conditions.
- [4. opus_token_count.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/opus/4.%20opus_token_count.ipynb) counts the number of tokens in the OPUS corpus for data analysis.
- [5. opus_languages_intersection_analysis.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/opus/5.%20opus_languages_intersection_analysis.ipynb) counts the number of language intersections in the OPUS corpus.
- [6. data_analysis.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/opus/6.%20data_analysis.ipynb) counts the number of senses suggested by one or two languages in the development set for data analysis.
- [7. error_analysis.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/opus/7.%20error_analysis.ipynb) counts senses suggested by certain languages based on evaluation set results for error analysis.
- [8. evaluation_set.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/opus/8.%20evaluation_set.ipynb) generates matching between OPUS and the evaluation set and runs the intersection algorithm using the best condition (condition 5).
- [classification_report_generator.py](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/opus/classification_report_generator.py) generates a classification report in the [`predictions_results`](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/opus/predictions_results) folder.

## wiktionary Folder

The [`wiktionary`](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/wiktionary) folder contains data related to the Wiktionary dataset. It is structured as follows:

### Subfolders:

- [data](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/wiktionary/data): This directory stores all the files of the original parallel data from SourceForge.
- [predictions_results](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/wiktionary/predictions_results): This is where the prediction results of the system's sense alignment are stored.

### Jupyter Notebooks:

- [1. wiktionary_extraction.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wiktionary/1.%20wiktionary_extraction.ipynb) parses data from the Wiktionary JSON file downloaded from [kaikki.org](https://kaikki.org/dictionary/English/index.html).
- [2. intersection_algorithm_wiktionary.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wiktionary/2.%20intersection_algorithm_wiktionary.ipynb) maps senses using the intersection algorithm on the Wiktionary data.
- [3. wiktionary_algorithm_based_conditions.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wiktionary/3.%20wiktionary_algorithm_based_conditions.ipynb) runs the mapped senses based on five conditions.
- [4. wiktionary_token_count.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wiktionary/4.%20wiktionary_token_count.ipynb) counts the number of tokens in the Wiktionary dataset for data analysis.
- [5. wiktionary_languages_intersection_analysis.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wiktionary/5.%20wiktionary_languages_intersection_analysis.ipynb) counts the number of language intersections in the Wiktionary dataset.
- [6. POS_analysis.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wiktionary/6.%20POS_analysis.ipynb) counts the number of parts of speech (POS) in Wiktionary for data analysis.
- [7. data_analysis.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wiktionary/7.%20data_analysis.ipynb) counts the number of senses suggested by one or two languages in the development set for data analysis.
- [8. evaluation_set.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wiktionary/8.%20evaluation_set.ipynb) generates matching between Wiktionary and the evaluation set and runs the intersection algorithm using the best condition (condition 5).
- [9. error_analysis.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wiktionary/9.%20error_analysis.ipynb) counts senses suggested by certain languages based on evaluation set results for error analysis.
- [classification_report_generator.py](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wiktionary/classification_report_generator.py) generates a classification report in the [`predictions_results`](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/wiktionary/predictions_results) folder.

## wn-msa-all Folder

The [`wn-msa-all`](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/wn-msa-all) folder contains data related to the main file (https://sourceforge.net/p/wn-msa/tab/HEAD/tree/trunk/) and additional data from Wordnet Bahasa maintainers. It is structured as follows:

### Subfolders:

- [data](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/wn-msa-all/data) stores all the files of the original parallel data from SourceForge.
- [predictions_results](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/wn-msa-all/predictions_results) stores prediction results of the system's sense alignment.

### Jupyter Notebooks:

- [1. development_evaluation_sets.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wn-msa-all/1.%20development_evaluation_sets.ipynb) builds development and evaluation sets.
- [2. goodness_labels_extraction.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wn-msa-all/2.%20goodness_labels_extraction.ipynb) extracts data from the main data (https://sourceforge.net/p/wn-msa/tab/HEAD/tree/trunk/) with labels B and I, extracting goodness labels to the development and evaluation sets.
- [3. combined_datasets_on_eval.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wn-msa-all/3.%20combined_datasets_on_eval.ipynb) combines both Wiktionary and OPUS data and runs the combined dataset on the evaluation set using the best condition. Generates a classification report.
- [4. wn-msa_error_analysis.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wn-msa-all/4.%20wn-msa_error_analysis.ipynb) suggests senses for the main data (https://sourceforge.net/p/wn-msa/tab/HEAD/tree/trunk/) using Wiktionary and OPUS data respectively for the final error analysis step. Takes 150 random samples from each data source.
- [5. error_analysis_hand-checked.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wn-msa-all/5.%20error_analysis_hand-checked.ipynb) obtains glosses of the 150 random samples and generates accuracy scores for both Wiktionary and OPUS for the last step of error analysis.
- [senses.ipynb](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wn-msa-all/senses.ipynb) checks senses, gloss, hypernym and hyponyms of a synset in WordNet for the purpose of further data anlysis.
- [classification_report_generator.py](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/wn-msa-all/classification_report_generator.py) generates a classification report in the [`predictions_results`](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/tree/main/wn-msa-all/predictions_results) folder.

## [requirement.txt](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/requirements.txt)
This file contains all the information about the packages needed to run the code. 

# Usage
To use this repository, first clone or download it to your local machine. Then, navigate to the respective folders based on your requirements. Each folder contains notebooks or scripts for specific tasks related to data analysis and intersection algorithms. Follow the instructions provided in the notebooks or scripts to execute the necessary operations.

# Contact
If you have any questions or encounter any issues, please feel free to reach out to the project owner at s.nurhalimah@student.vu.nl

# [License.txt](https://github.com/iamima188/Siti_Nurhalimah_Thesis_2023/blob/main/LICENSE.txt)
Licence of the repository 
