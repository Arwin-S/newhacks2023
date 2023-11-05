from tensorflow_lite_support.metadata import metadata_schema_py_generated as _metadata_fb
from tensorflow_lite_support.metadata import schema_py_generated as _schema_fb
from flatbuffers import Encode
from flatbuffers import Table

# Load TensorFlow Lite model and metadata.
with open("object_detection_mobile_object_localizer_v1_1_default_1.tflite", "rb") as f:
    model_with_metadata = f.read()

# Find the metadata buffer in the model file.
model = _schema_fb.Model.GetRootAsModel(model_with_metadata, 0)
metadata_list = [model.Metadata(i) for i in range(model.MetadataLength())]
metadata = next((x for x in metadata_list if x.Name() == "name_of_the_metadata"), None)

# Parse the metadata buffer using the schema for TFLite Metadata.
meta_buffer = metadata.Buffer()
metadata_fb = _metadata_fb.ModelMetadata.GetRootAsModelMetadata(meta_buffer.Bytes, meta_buffer.Pos)

# Extract information as needed.
print(metadata_fb.Description())
print(metadata_fb.Version())
# ... and other fields based on the metadata schema
