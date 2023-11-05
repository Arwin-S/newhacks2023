import json

# The metadata_json string you got from the earlier output
metadata_json_str = '''{
  "name": "Mobile Object Localizer",
  "description": "Identify which of a known set of objects might be present and provide information about their positions within the given image or a video stream.",
  "version": "v1",
  "subgraph_metadata": [
    {
      "input_tensor_metadata": [
        {
          "name": "image",
          "description": "Input image to be detected. The expected image is 192 x 192, with three channels (red, blue, and green) per pixel. Each value in the tensor is a single byte between 0 and 255.",
          "content": {
            "content_properties_type": "ImageProperties",
            "content_properties": {
              "color_space": "RGB"
            }
          },
          "process_units": [
            {
              "options_type": "NormalizationOptions",
              "options": {
                "mean": [
                  127.5
                ],
                "std": [
                  127.5
                ]
              }
            }
          ],
          "stats": {
            "max": [
              255.0
            ],
            "min": [
              0.0
            ]
          }
        }
      ],
      "output_tensor_metadata": [
        {
          "name": "location",
          "description": "The locations of the detected boxes.",
          "content": {
            "content_properties_type": "BoundingBoxProperties",
            "content_properties": {
              "index": [
                1,
                0,
                3,
                2
              ],
              "type": "BOUNDARIES"
            },
            "range": {
              "min": 2,
              "max": 2
            }
          }
        },
        {
          "name": "category",
          "description": "The categories of the detected boxes.",
          "content": {
            "content_properties_type": "FeatureProperties",
            "content_properties": {
            },
            "range": {
              "min": 2,
              "max": 2
            }
          },
          "associated_files": [
            {
              "name": "labelmap.txt",
              "description": "Label of objects that this model can recognize.",
              "type": "TENSOR_VALUE_LABELS"
            }
          ]
        },
        {
          "name": "score",
          "description": "The scores of the detected boxes.",
          "content": {
            "content_properties_type": "FeatureProperties",
            "content_properties": {
            },
            "range": {
              "min": 2,
              "max": 2
            }
          }
        },
        {
          "name": "number of detections",
          "description": "The number of the detected boxes.",
          "content": {
            "content_properties_type": "FeatureProperties",
            "content_properties": {
            }
          }
        }
      ]
    }
  ],
  "author": "TensorFlow",
  "license": "Apache License. Version 2.0 http://www.apache.org/licenses/LICENSE-2.0."
}'''

# Convert JSON string to a Python dictionary
metadata_dict = json.loads(metadata_json_str)

# Access the parts of metadata as needed
print("Model Name:", metadata_dict["name"])
print("Model Description:", metadata_dict["description"])
print("Model Version:", metadata_dict["version"])

# Loop through input tensor metadata
for input_tensor in metadata_dict["subgraph_metadata"][0]["input_tensor_metadata"]:
    print("Input Tensor Name:", input_tensor["name"])
    # ... and so on for other fields

# Loop through output tensor metadata
for output_tensor in metadata_dict["subgraph_metadata"][0]["output_tensor_metadata"]:
    print("Output Tensor Name:", output_tensor["name"])
    # ... and so on for other fields

# You can do the same for the author, license, etc.

# If there are associated files, you might need to load them separately
# Here's how you could access the name of an associated file:
for output_tensor in metadata_dict["subgraph_metadata"][0]["output_tensor_metadata"]:
    if "associated_files" in output_tensor:
        for associated_file in output_tensor["associated_files"]:
            print("Associated File Name:", associated_file["name"])
            # You could then open and read the contents of the file if needed
