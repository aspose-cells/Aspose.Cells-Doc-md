---
title: 在Ruby中加密Excel文件
type: docs
weight: 80
url: /zh/java/encrypting-excel-files-in-ruby/
---

## **Aspose.Cells - 加密Excel文件**
要在Ruby中使用Aspose.Cells for Java对Excel文件应用加密，只需调用Encrypt模块即可。

**Ruby 代码**

{{< highlight ruby >}}

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
从以下任何社交编码网站下载**加密Excel文件（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/encrypt.rb)
