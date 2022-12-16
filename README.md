# uPrintApi

Api for generating microprints of text files with rules from a configuration JSON file.

## Generating a microprint
The only important endpoint present is the one for generating microprints. 

| Method        | url                    | Body  |
| ------------- |:-------------:         | -----:|
|  `POST`       | `microprint/generate`  | The body consists of a formData with two files. One called `text_file` with the text file to generate the microprint from and one called `config_file` which corresponds to the configuration JSON file with the rules of the microprint.      |