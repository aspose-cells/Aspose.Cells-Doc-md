---
title: Satır ve Sütunları Otomatik Uydur
type: docs
weight: 20
url: /tr/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excel, hücrenin içeriğine göre genişlik ve yüksekliği Otomatik Ayarlamak için iyi bir özellik sağlar. Bu özellik, Aspose.Cells kullanıcılarına da çalışma zamanında bir hücrenin boyutlarını otomatik olarak ayarlama olanağı sunuyor.

{{% /alert %}} 
## **Otomatik Uydurma**
Aspose.Cells, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) adında bir Microsoft Excel dosyasını temsil eden bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) kolleksiyonuna sahiptir.

Bir çalışma sayfası [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, çalışma sayfasını yönetmek için geniş bir yelpazede özellikler ve yöntemler sağlar. Bu makale, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfını kullanarak satırları veya sütunları otomatik olarak uyarlama konusuna bakmaktadır.
### **Satırı Otomatik Uydurma - Basit**
Bir satırın otomatik olarak genişlik ve yükseklik ayarlama yaklaşımındaki en doğrudan yol, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfının [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) metodunu çağırmaktır. [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) metodu, yeniden boyutlandırılacak satırın dizinini (satır indeksini) parametre olarak alır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Hücrelerin Aralığında Satırı Otomatik Uydur**
Bir satır, birçok sütundan oluşur. Aspose.Cells, geliştiricilerin, satır içindeki hücre aralığındaki içerik temel alınarak satırın yüksekliğini otomatik ayarlamalarını sağlar ve bu işlevselliği sağlamak için [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) metodunun aşırı yüklenmiş versiyonunu çağırabilir. Bu metod aşağıdaki parametreleri alır:

- **Satır dizini**, otomatik olarak uyarlama yapılacak satırın dizini.
- **İlk sütun dizini**, satırın ilk sütununun dizini.
- **Son sütun dizini**, satırın son sütununun dizini.

[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) metodu, satırdaki tüm sütunların içeriğini kontrol eder ve ardından satırı otomatik olarak ayarlar.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Kolay Otomatik Uydurma**
Bir sütunun genişliğini ve yüksekliğini otomatik ayarlamanın en kolay yolu, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfının [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) metodunu çağırmaktır. [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) metodu, yeniden boyutlandırılacak sütunun indeksini parametre olarak alır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Hücre Aralığındaki Otomatik Uydurma Sütunu**
Bir sütun, birçok satırdan oluşur. İçeriğe göre otomatik olarak ayarlamak için, [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) metodu, aşağıdaki parametreleri alan aşırı yüklenmiş versiyonunu çağırabilirsiniz:

- **Sütun indeksi**, otomatik olarak uygun hale getirilmesi gereken sütunun indeksini temsil eder
- **İlk satır indeksi**, sütunun ilk satırının indeksini temsil eder.
- **Son satır indeksi**, sütunun son satırının indeksini temsil eder.

[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) metodu, tüm satırların içeriğini kontrol eder ve ardından sütunu otomatik olarak ayarlar.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Birleştirilmiş Hücreler için Satırları Otomatik Uydurma**
Aspose.Cells ile [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API'sını kullanarak birleştirilmiş hücreler için satırları otomatik olarak genişletebilirsiniz. [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) sınıfı, birleştirilmiş hücreler için satırları otomatik olarak genişletmek için kullanılabilecek bir [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) özelliğini sağlar. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType), aşağıdaki üyelere sahip olan bir [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) numaralandırmayı kabul eder:

- [YOK](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Birleştirilmiş hücreleri yok sayar.
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST-LINE): yalnızca ilk satırın yüksekliğini genişletir.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST-LINE): Sadece son satırın yüksekliğini genişletir.
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH-LINE): Her satırın yüksekliğini sadece genişletir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

Ayrıca, [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows--) ve [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns--) metodlarının aşırı yüklenmiş sürümlerini kullanabilirsiniz. Bu sürümler belirli satır/ sütun aralığını ve bir [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) örneğini kabul eder ve seçilen satır/sütunların uygun [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) ayarlarıyla otomatik ayarlanmasını sağlar.

Yukarıda bahsedilen metodların imzaları aşağıdaki gibidir:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Bilinmesi Gerekenler**
{{% alert color="primary" %}} 

Bir hücre birleşmişse, *AutoFit* metodları uygulanmayacaktır, bu Microsoft Excel'deki davranışla aynıdır. Ayrıca, hücredeki metin katlanmışsa, [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) metodu da uygulanmaz. Bir diğer bilmeniz gereken şey ise, *AutoFit* metodlarının zaman alıcı olmasıdır. Bu yüzden, metodları olabildiğince az çağırmanız, uygulamanızın verimliliği açısından önemlidir.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
