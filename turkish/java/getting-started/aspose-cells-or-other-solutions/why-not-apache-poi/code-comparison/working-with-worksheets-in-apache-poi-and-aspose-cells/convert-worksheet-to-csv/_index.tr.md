﻿---
title: Çalışma Sayfasını CSV'e Dönüştür
type: docs
weight: 30
url: /tr/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Çalışma Sayfasını CSV'e Dönüştür**
Geliştiricilerin dosyalarını bir depolama konumuna kaydetmeleri gerekiyorsa, dosya adını (tam depolama yolu ile birlikte) ve istenen dosya biçimini (kullanarak) belirtebilirler.**Dosya Biçimi Türü**numaralandırma) çağrılırken**kayıt etmek**yöntemi**Çalışma kitabı**nesne.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Çalışma Sayfasını CSV'e Dönüştür**
Aşağıdaki kod, çalışma sayfasının Aspose.Cells Java API ile karşılaştırıldığında Apache POI HSSF ve XSSF API kullanılarak CSV'e nasıl dönüştürülebileceğini gösterir.

**Java**

{{< highlight "java" >}}

 /**

\* Temel bir XLSX -> CSV işlemci

\* POI örnek programı XLS2CSVmra, Nick Burch tarafından

\* org.apache.poi.hssf.eventusermodel.examples paketi.

\* HSSF versiyonundan farklı olarak, bu tamamen yok sayar

\* eksik satırlar.

\* <p/>

\* Veri sayfaları, SAX çözümleyici kullanılarak okunur.

\* bellek alanı nispeten küçük, yani bu olmalı

\* çok büyük çalışma kitaplarını okuyabilir. Stiller tablosu ve

\* paylaşılan dize tablosu bellekte tutulmalıdır. bu

\* standart POI stilleri tablo sınıfı kullanılır, ancak özel

\* (salt okunur) sınıfı, paylaşılan dize tablosu için kullanılır

\* çünkü standart POI SharedStringsTable çok büyür

\* benzersiz dizelerin sayısıyla hızlı bir şekilde.

\* <p/>

\* Bir sorunu çözen yama için Eric Smith'e teşekkürler

\* birden çok "t" öğesi olan hücreler tarafından tetiklenir;

\* Excel'in farklı biçimleri nasıl temsil ettiği (örneğin, bir sözcük

\* düz ve bir kelime kalın).

\*

\* @yazar Chris Lott

*/

public class ApacheXLSX2CSV {