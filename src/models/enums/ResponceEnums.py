from enum import Enum

class ResponceSignal(Enum):
    
    FILE_VALIDATED_SUCCESS = "file_validated_successfully"
    FILE_TYPE_NOT_SUPPORTED = "File_type _not_supported"
    FILE_SIZE_EXCEEDED = "file_size _exceeded "
    FILE_UPLOADED_SUCCESS = "Success"
    FILE_UPLOADED_FAIL = "Faild"
