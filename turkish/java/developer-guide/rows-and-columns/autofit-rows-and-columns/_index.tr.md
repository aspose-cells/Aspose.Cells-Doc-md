---
title: Satırları ve Sütunları Otomatik Sığdır
type: docs
weight: 20
url: /tr/java/autofit-rows-and-columns/
---
{{% alert color="primary" %}} 

Microsoft Excel, bir hücrenin genişliğini ve yüksekliğini içeriğine göre Otomatik Boyutlandırmak için iyi bir özellik sağlar. Bu özellik aynı zamanda Aspose.Cells kullanıcılarına, çalışma zamanında bir hücrenin boyutlarını otomatik boyutlandırma gücüyle de sunulmaktadır.

{{% /alert %}} 
## **Otomatik Uydurma**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[çalışma sayfaları](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bu makale,[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)satırları veya sütunları otomatik sığdırmak için sınıf.
### **Satırı Otomatik Sığdır - Basit**
 Bir satırın genişliğini ve yüksekliğini otomatik olarak boyutlandırmak için en doğrudan yaklaşım,[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf'[Otomatik Sığdır](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\) ) yöntem. bu[Otomatik Sığdır](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) yöntemi, parametre olarak (yeniden boyutlandırılacak satırın) bir satır dizinini alır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Cells aralığında AutoFit Row**
 Bir satır birçok sütundan oluşur. Aspose.Cells, geliştiricilerin aşırı yüklenmiş bir sürümünü çağırarak satırdaki bir hücre aralığındaki içeriğe dayalı olarak bir satırı otomatik olarak sığdırmasına olanak tanır.[Otomatik Sığdır](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) yöntem. Aşağıdaki parametreleri alır:

- **Satır dizini**, otomatik sığdırılacak satırın dizini.
- **İlk sütun dizini**, satırın ilk sütununun dizini.
- **Son sütun dizini**, satırın son sütununun dizini.

 bu[Otomatik Sığdır](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) yöntemi, satırdaki tüm sütunların içeriğini kontrol eder ve ardından satıra otomatik sığdırır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Otomatik Sığdırma Sütunu - Basit**
 Bir sütunun genişliğini ve yüksekliğini otomatik olarak boyutlandırmanın en kolay yolu,[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf'[Otomatik SığdırSütunu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) yöntem. bu[Otomatik SığdırSütunu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)yöntemi, sütun indeksini (yeniden boyutlandırılmak üzere olan sütunun) parametre olarak alır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Cells Aralığında Otomatik Sığdırma Sütunu**
 Bir sütun birçok satırdan oluşur. Aşırı yüklenmiş bir sürümünü çağırarak, sütundaki bir hücre aralığındaki içeriğe dayalı olarak bir sütunu otomatik olarak sığdırmak mümkündür.[Otomatik SığdırSütunu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) aşağıdaki parametreleri alan yöntem:

- **Sütun dizini**, içeriği otomatik olarak sığdırılması gereken sütunun dizinini temsil eder
- **İlk satır dizini**, sütunun ilk satırının dizinini temsil eder
- **Son satır dizini**, sütunun son satırının dizinini temsil eder

 bu[Otomatik SığdırSütunu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) yöntemi, sütundaki tüm satırların içeriğini kontrol eder ve ardından sütunu otomatik olarak sığdırır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Birleştirilmiş Cells için Satırları Otomatik Sığdır**
Aspose.Cells ile, kullanılarak birleştirilmiş hücreler için bile satırları otomatik sığdırmak mümkündür.[Otomatik Sığdırma Seçenekleri](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [Otomatik Sığdırma Seçenekleri](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)sınıf sağlar[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)satırları birleştirilmiş hücrelere otomatik sığdırmak için kullanılabilen özellik.[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)kabul eder[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)aşağıdaki üyelere sahip numaralandırılabilir.

- [YOK](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Birleştirilmiş hücreleri yok sayın.
- [İLK SATIR](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Yalnızca ilk satırın yüksekliğini genişletir.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Yalnızca son satırın yüksekliğini genişletir.
- [HER ÇİZGİ](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): Yalnızca her satırın yüksekliğini genişletir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

 Aşırı yüklenmiş sürümlerini de kullanabilirsiniz.[Otomatik SığdırSatırlar](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [Otomatik SığdırSütunlar](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\) ) bir satır/sütun aralığını ve örneğini kabul eden yöntemler[Otomatik Sığdırma Seçenekleri](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) seçilen satırları/sütunları istenen şekilde otomatik sığdırmak için[Otomatik Sığdırma Seçenekleri](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)buna göre.

Söz konusu yöntemlerin imzaları aşağıdaki gibidir:

1.  autoFitRows(int startRow, int endRow,[Otomatik Sığdırma Seçenekleri](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)seçenekler)
1.  autoFitColumns(int firstColumn, int lastColumn,[Otomatik Sığdırma Seçenekleri](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)seçenekler)
## **Bilmeniz Önemli**
{{% alert color="primary" %}} 

 Bir hücre birleştirilirse, o zaman*Otomatik Sığdır* Microsoft Excel'deki ile aynı davranış olan yöntemler uygulanmaz. Ayrıca, bir hücredeki metin kaydırılırsa,[Otomatik SığdırSütunu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) yöntemi de uygulanmayacaktır. Bilmeniz gereken başka bir şey de,*Otomatik Sığdır*yöntemler zaman alıcıdır. Bu nedenle, uygulamanızın verimliliğini sağlamak için bu yöntemleri mümkün olduğunca nadiren çağırmalısınız.

{{% /alert %}}
