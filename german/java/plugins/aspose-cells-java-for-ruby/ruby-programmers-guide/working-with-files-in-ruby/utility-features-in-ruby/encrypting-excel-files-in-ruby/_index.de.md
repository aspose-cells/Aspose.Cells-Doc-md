---
title: Verschlüsselung von Excel Dateien in Ruby
type: docs
weight: 80
url: /de/java/encrypting-excel-files-in-ruby/
---

## **Aspose.Cells - Verschlüsselung von Excel-Dateien**
Um Verschlüsselung auf Excel-Dateien mithilfe von Aspose.Cells for Java in Ruby anzuwenden, rufen Sie einfach das Encrypt-Modul auf.

**Ruby-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Verschlüsselung von Excel-Dateien (Aspose.Cells)** von einer der unten genannten Social-Coding-Seiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/encrypt.rb)
