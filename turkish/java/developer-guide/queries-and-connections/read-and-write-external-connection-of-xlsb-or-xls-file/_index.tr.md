---
title: XLSB veya XLS dosyasının Harici Bağlantısını Okuma ve Yazma
type: docs
weight: 80
url: /tr/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells halihazırda XLSX dosyasının harici bağlantısını okuma ve yazma özelliğini desteklemektedir, ancak şimdi bu özelliği XLSB ve XLS dosyası için de desteklemektedir. Ancak, kod her iki biçim türü için de aynıdır.

## **XLSB/XLS dosyasının Harici Bağlantısını Okuma ve Yazma**

Aşağıdaki örnek kod, örnek XLSB(XLS de yüklenebilir) dosyasını yükler ve aslında bir Microsoft Access DB Bağlantısı olan ilk Harici Bağlantısını okur. Daha sonra değiştirir[**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name)özelliğinden yararlanır ve onu çıktı XLSB dosyası olarak kaydeder. Ekran görüntüsü, kodun etkisini gösterir.[örnek XLSB dosyası](51740743.xlsb)ve[çıktı XLSB dosyası](51740742.xlsb)infazından sonra. Lütfen referans için aşağıda verilen örnek kodun konsol çıktısına da bakın.

![yapılacaklar:resim_alternatif_Metin](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **Basit kod**

Aşağıdaki kod, uygun uzantıya sahip dosyaları yükleyip kaydederek hem XLSB hem de XLS için çalışacaktır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
