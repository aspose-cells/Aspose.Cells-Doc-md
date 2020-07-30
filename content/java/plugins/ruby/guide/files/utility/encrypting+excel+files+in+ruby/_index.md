---
title : "Encrypting Excel Files in Ruby" 
description : "" 
weight : 24707 
toc : false
type: docs
url: /java/plugins/ruby/guide/files/utility/encrypting+excel+files+in+ruby/
---

# Aspose.Cells for Java : Encrypting Excel Files in Ruby


## Aspose.Cells - Encrypting Excel Files

To apply encryption to Excel files using Aspose.Cells for Java in Ruby, simply invoke Encrypt module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object by excel file pathworkbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')# Password protect the file.workbook.getSettings().setPassword("1234")encryption\_type = Rjb::import('com.aspose.cells.EncryptionType')        # Specify XOR encrption type.workbook.setEncryptionOptions(encryption\_type.XOR, 40)# Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).workbook.setEncryptionOptions(encryption\_type.STRONG\_CRYPTOGRAPHIC\_PROVIDER, 128)# Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(data\_dir + "encrypt.xls")puts "Apply encryption, please check the output file."

## Download Running Code

Download **Encrypting Excel Files (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/encrypt.rb)

