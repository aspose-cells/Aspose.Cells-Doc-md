---
title: 在 Ruby 中加密 Excel 文件
type: docs
weight: 80
url: /zh/java/encrypting-excel-files-in-ruby/
---
## **Aspose.Cells - 加密 Excel 文件**
要在 Ruby 中使用 Aspose.Cells for Java 对 Excel 文件应用加密，只需调用 Encrypt 模块。

**红宝石代码**

{{< highlight "ruby" >}}

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

{{< /highlight >}}
## **下载运行代码**
下载**加密 Excel 文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/encrypt.rb)
