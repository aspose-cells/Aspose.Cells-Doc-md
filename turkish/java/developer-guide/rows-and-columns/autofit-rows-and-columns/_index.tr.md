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
Bir satırın genişlik ve yüksekliğini otomatik olarak ayarlamanın en basit yaklaşımı, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfının [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) yöntemini çağırmaktır. [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) yöntemi, bir parametre olarak bir satır dizini (yeniden boyutlandırılacak satırın dizini) alır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Hücrelerin Aralığında Satırı Otomatik Uydur**
Bir satır, birçok sütundan oluşur. Aspose.Cells, geliştiricilere bir satırın içindeki hücrelerin bir aralığındaki içeriğe bağlı olarak bir satırı otomatik olarak uyarlama olanağı sağlar. Bu, [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) yönteminin birden fazla parametre alan aşırı yüklenmiş bir sürümünü çağırarak gerçekleştirilir. Aşağıdaki parametreleri alır:

- **Satır dizini**, otomatik olarak uyarlama yapılacak satırın dizini.
- **İlk sütun dizini**, satırın ilk sütununun dizini.
- **Son sütun dizini**, satırın son sütununun dizini.

The [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) metodu, satırdaki tüm sütunların içeriğini kontrol eder ve ardından satırı otomatik olarak uygun hale getirir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Kolay Otomatik Uydurma**
Bir sütunun genişlik ve yüksekliğini otomatik olarak ayarlamanın en kolay yolu, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfının [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) metodunu çağırmaktır. [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) metodu, genişletilecek sütunun sütun indeksini parametre olarak alır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Hücre Aralığındaki Otomatik Uydurma Sütunu**
Bir sütun, birçok satırdan oluşur. [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) metodunun aşırı yüklenmiş bir versiyonunu çağırarak bir sütundaki hücre aralığındaki içeriğe göre bir sütunu otomatik olarak uydurmak mümkündür. Bu versiyon, aşağıdaki parametreleri alan bir [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) metodunu alır:

- **Sütun indeksi**, otomatik olarak uygun hale getirilmesi gereken sütunun indeksini temsil eder
- **İlk satır indeksi**, sütunun ilk satırının indeksini temsil eder.
- **Son satır indeksi**, sütunun son satırının indeksini temsil eder.

[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) metodu, tüm sütundaki tüm satırların içeriğini kontrol eder ve ardından sütunu otomatik olarak uygun hale getirir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Birleştirilmiş Hücreler için Satırları Otomatik Uydurma**
Aspose.Cells ile [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API'sını kullanarak birleştirilmiş hücreler için satırları otomatik olarak genişletebilirsiniz. [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) sınıfı, birleştirilmiş hücreler için satırları otomatik olarak genişletmek için kullanılabilecek bir [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) özelliğini sağlar. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType), aşağıdaki üyelere sahip olan bir [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) numaralandırmayı kabul eder:

- [YOK](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Birleştirilmiş hücreleri yok sayar.
- [İLK_SATIR](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Sadece ilk satırın yüksekliğini genişletir.
- [SON_SATIR](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Sadece son satırın yüksekliğini genişletir.
- [HER_SATIR](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): Her satırın yüksekliğini genişletir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

Seçilen satırları/sütunları ve istenen [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) ile otomatik olarak uygun hale getirmek için [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) ve [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\)) metodlarının aşırı yüklenmiş versiyonlarını ve [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) örneğini kullanabilirsiniz.

Yukarıda bahsedilen metodların imzaları aşağıdaki gibidir:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Bilinmesi Gerekenler**
{{% alert color="primary" %}} 

Bir hücre birleştirilmişse, *OtoUydur* metodları uygulanmaz, bu da Microsoft Excel'de olduğu gibi aynı davranıştır. Ayrıca, bir hücredeki metin kaydırılmışsa, [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) metodu da uygulanmaz. Bir diğer bilmeniz gereken şey de *OtoUydur* metodlarının zaman alıcı olmasıdır. Bu nedenle, uygulamanızın verimliliğini sağlamak için bu metodları mümkün olduğunca nadir aramalısınız.

{{% /alert %}}
