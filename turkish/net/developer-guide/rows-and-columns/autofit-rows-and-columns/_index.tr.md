---
title: Satırları ve Sütunları Otomatik Sığdır
type: docs
weight: 20
url: /tr/net/autofit-rows-and-columns/
description: Bu makalede satırların, sütunların, birleştirilmiş hücre satırlarının ve bir hücre aralığındaki satırların Aspose.Cells for .NET API ile nasıl otomatik sığdırılacağı gösterilmektedir.
keywords: Autofit rows, autofit columns, autofit row in a range of cells, autofit rows of merged cells
---
{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların hücrelerin genişliğini ve yüksekliğini içeriğe göre otomatik olarak boyutlandırmasına olanak tanır. Bu özellik aynı zamanda Aspose.Cells aracılığıyla da mevcuttur, böylece geliştiriciler çalışma zamanında bir hücrenin boyutlarını otomatik olarak boyutlandırabilir.

{{% /alert %}}

##  **Otomatik Montaj**

Aspose.Cells şunları sağlar:[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel dosyasını temsil eden sınıf.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Bir Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bu makale,[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Satırları veya sütunları otomatik olarak sığdırmak için sınıf.

###  **Satırı Otomatik Sığdır - Basit**

 Bir satırın genişliğini ve yüksekliğini otomatik olarak boyutlandırmaya yönelik en basit yaklaşım,[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**Otomatik SığdırSatırı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) yöntem.[**Otomatik SığdırSatırı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)yöntem parametre olarak (yeniden boyutlandırılacak satırın) satır dizinini alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

###  **Cells Aralığında Satırı Otomatik Sığdırma**

 Bir satır birçok sütundan oluşur. Aspose.Cells, geliştiricilerin, satırın aşırı yüklenmiş bir sürümünü çağırarak satır içindeki bir hücre aralığındaki içeriğe dayalı olarak bir satırı otomatik olarak sığdırmasına olanak tanır.[**Otomatik SığdırSatırı**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)yöntem. Aşağıdaki parametreleri alır:

- *Satır dizini**, otomatik olarak sığdırılmak üzere olan satırın dizini.
- *İlk sütun dizini**, satırın ilk sütununun dizini.
- *Son sütun dizini**, satırın son sütununun dizini.

[**Otomatik SığdırSatırı**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)yöntemi satırdaki tüm sütunların içeriğini kontrol eder ve ardından satıra otomatik olarak sığar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

###  **Sütunu Cells Aralığında Otomatik Olarak Sığdırma**

 Bir sütun birçok satırdan oluşur. Aşırı yüklenmiş bir sürümünü çağırarak, sütundaki bir hücre aralığındaki içeriğe dayalı olarak bir sütunu otomatik olarak sığdırmak mümkündür.[**Otomatik SığdırSütunu**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)Aşağıdaki parametreleri alan yöntem:

- *Sütun dizini**, otomatik olarak sığdırılmak üzere olan sütunun dizini.
- *İlk satır dizini**, sütunun ilk satırının dizini.
- *Son satır dizini**, sütunun son satırının dizini.

[**Otomatik SığdırSütunu**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)yöntemi sütundaki tüm satırların içeriğini kontrol eder ve ardından sütuna otomatik olarak sığar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

###  **Birleştirilmiş Cells için Satırları Otomatik Sığdırma**

 Aspose.Cells ile, kullanılarak birleştirilmiş hücreler için bile satırları otomatik olarak sığdırmak mümkündür.[**Otomatik Montaj Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**Otomatik Montaj Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)sınıf sağlar[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) Birleştirilmiş hücrelere ilişkin satırları otomatik olarak sığdırmak için kullanılabilecek özellik.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)kabul eder[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) aşağıdaki üyelere sahip numaralandırılabilir.

- Yok: Birleştirilmiş hücreleri yoksay.
- FirstLine: Yalnızca ilk satırın yüksekliğini genişletir.
- LastLine: Yalnızca son satırın yüksekliğini genişletir.
- EveryLine: Yalnızca her satırın yüksekliğini genişletir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Ayrıca aşırı yüklenmiş sürümlerini kullanmayı da deneyebilirsiniz.[**Otomatik SığdırSatırları**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**Sütunları Otomatik Sığdır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) bir dizi satır/sütun ve bir örneğini kabul eden yöntemler[**Otomatik Montaj Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) seçilen satırları/sütunları istediğiniz gibi otomatik olarak sığdırmak için[**Otomatik Montaj Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)buna göre.

Söz konusu yöntemlerin imzaları aşağıdaki gibidir:

1.  AutoFitRows(int startRow, int endRow,[**Otomatik Montaj Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)seçenekler)
1.  AutoFitColumns(int FirstColumn, int lastColumn,[**Otomatik Montaj Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)seçenekler)

{{% /alert %}}

##  **Bilmeniz Önemli**

{{% alert color="primary" %}}

Bir hücre birleştirilirse Otomatik Sığdırma yöntemleri uygulanmaz; bu, Microsoft Excel'deki davranışın aynısıdır. API otomatik filtresini kullanarak bu sorunu çözebilirsiniz. Ayrıca, bir hücredeki metin kaydırılmışsa,[**Otomatik SığdırSütunu**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) yöntem de uygulanmayacaktır. Bilmeniz gereken bir diğer şey ise*Otomatik Sığdır*yöntemler zaman alıcıdır. Bu nedenle, uygulamanızın verimliliğini sağlamak için bu yöntemleri mümkün olduğunca nadiren çağırmalısınız.

{{% /alert %}}

##  **İleri konular**
- [Birleştirilmiş Satırları Otomatik Sığdır Cells](/cells/tr/net/autofit-rows-for-merged-cells/)
