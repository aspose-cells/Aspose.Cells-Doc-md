---
title: Crittografare i file Excel in Ruby
type: docs
weight: 80
url: /it/java/encrypting-excel-files-in-ruby/
---
## **Aspose.Cells - Crittografia file Excel**
Per applicare la crittografia ai file Excel utilizzando Aspose.Cells for Java in Ruby, è sufficiente richiamare il modulo Encrypt.

**Codice Rubino**

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
## **Scarica il codice in esecuzione**
Scaricamento**Crittografia file Excel (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/encrypt.rb)
