##Encrypting Excel Files in Ruby
## **Aspose.Cells - Encrypting Excel Files**
To apply encryption to Excel files using Aspose.Cells for Java in Ruby, simply invoke Encrypt module.
**Ruby Code**
data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
\# Instantiating a Workbook object by excel file path
workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')
\# Password protect the file.
workbook.getSettings().setPassword("1234")
encryption_type = Rjb::import('com.aspose.cells.EncryptionType')
\# Specify XOR encrption type.
workbook.setEncryptionOptions(encryption_type.XOR, 40)
\# Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(encryption_type.STRONG_CRYPTOGRAPHIC_PROVIDER, 128)
\# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(data_dir + "encrypt.xls")
puts "Apply encryption, please check the output file."
## **Download Running Code**
Download **Encrypting Excel Files (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/encrypt.rb)
