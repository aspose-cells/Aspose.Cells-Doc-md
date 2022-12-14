---
title: Satırları ve Sütunları Otomatik Sığdır
type: docs
weight: 20
url: /tr/net/autofit-rows-and-columns/
---
{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların içeriğine göre hücrelerin genişliğini ve yüksekliğini otomatik olarak boyutlandırmasını sağlar. Bu özellik aynı zamanda Aspose.Cells aracılığıyla da mevcuttur, böylece geliştiriciler çalışma zamanında bir hücrenin boyutlarını otomatik olarak boyutlandırabilir.

{{% /alert %}}

## **Otomatik Uydurma**

Aspose.Cells bir sağlar[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel dosyasını temsil eden sınıf. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bu makale,[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)satırları veya sütunları otomatik sığdırmak için sınıf.

### **Satırı Otomatik Sığdır - Basit**

 Bir satırın genişliğini ve yüksekliğini otomatik olarak boyutlandırmak için en doğrudan yaklaşım,[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf[**Satırı Otomatik Sığdır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) yöntem. bu[**Satırı Otomatik Sığdır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)yöntem, parametre olarak (yeniden boyutlandırılacak satırın) bir satır dizinini alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Cells aralığında AutoFit Row**

 Bir satır birçok sütundan oluşur. Aspose.Cells, geliştiricilerin aşırı yüklenmiş bir sürümünü çağırarak satırdaki bir hücre aralığındaki içeriğe dayalı olarak bir satırı otomatik olarak sığdırmasına olanak tanır.[**Satırı Otomatik Sığdır**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)yöntem. Aşağıdaki parametreleri alır:

- **Satır dizini**, otomatik sığdırılacak satırın dizini.
- **İlk sütun dizini**, satırın ilk sütununun dizini.
- **Son sütun dizini**, satırın son sütununun dizini.

 bu[**Satırı Otomatik Sığdır**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)yöntem, satırdaki tüm sütunların içeriğini kontrol eder ve ardından satıra otomatik olarak sığdırır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Cells Aralığında Otomatik Sığdırma Sütunu**

 Bir sütun birçok satırdan oluşur. Aşırı yüklenmiş bir sürümünü çağırarak, sütundaki bir hücre aralığındaki içeriğe dayalı olarak bir sütunu otomatik olarak sığdırmak mümkündür.[**Otomatik Sığdırma Sütunu**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)aşağıdaki parametreleri alan yöntem:

- **Sütun dizini**otomatik olarak sığdırılacak sütunun dizini.
- **İlk satır dizini**, sütunun ilk satırının dizini.
- **Son satır dizini**, sütunun son satırının dizini.

 bu[**Otomatik Sığdırma Sütunu**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)yöntem, sütundaki tüm satırların içeriğini kontrol eder ve ardından sütunu otomatik olarak sığdırır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Birleştirilmiş Cells için Satırları Otomatik Sığdır**

 Aspose.Cells ile, kullanılarak birleştirilmiş hücreler için bile satırları otomatik sığdırmak mümkündür.[**Otomatik Sığdırma Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**Otomatik Sığdırma Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)sınıf sağlar[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) satırları birleştirilmiş hücrelere otomatik sığdırmak için kullanılabilen özellik.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)kabul eder[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) aşağıdaki üyelere sahip numaralandırılabilir.

- Yok: Birleştirilmiş hücreleri yok sayın.
- FirstLine: Yalnızca ilk satırın yüksekliğini genişletir.
- LastLine: Yalnızca son satırın yüksekliğini genişletir.
- EveryLine: Yalnızca her satırın yüksekliğini genişletir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Ayrıca aşırı yüklenmiş sürümlerini kullanmayı deneyebilirsiniz.[**Satırları Otomatik Sığdır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**Sütunları Otomatik Sığdır**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) bir satır/sütun aralığını ve örneğini kabul eden yöntemler[**Otomatik Sığdırma Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) seçilen satırları/sütunları istediğiniz şekilde otomatik sığdırmak için[**Otomatik Sığdırma Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)buna göre.

Söz konusu yöntemlerin imzaları aşağıdaki gibidir:

1.  AutoFitRows(int startRow, int endRow,[**Otomatik Sığdırma Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)seçenekler)
1. AutoFitColumns(int firstColumn, int lastColumn,[**Otomatik Sığdırma Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)seçenekler)

{{% /alert %}}

## **Bilmeniz Önemli**

{{% alert color="primary" %}}

 Bir hücre birleştirilirse, Microsoft Excel'deki ile aynı davranış olan Otomatik Sığdırma yöntemleri uygulanmaz. API otomatik filtresini kullanarak bu sorunu çözebilirsiniz. Ayrıca, bir hücredeki metin kaydırılırsa,[**Otomatik Sığdırma Sütunu**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) yöntem de uygulanmayacaktır. Bilmeniz gereken başka bir şey de,*Otomatik Sığdır*yöntemler zaman alıcıdır. Bu nedenle, uygulamanızın verimliliğini sağlamak için bu yöntemleri mümkün olduğunca nadiren çağırmalısınız.

{{% /alert %}}

## **ileri konular**
- [Birleştirilmiş Cells için Satırları Otomatik Sığdır](/cells/tr/net/autofit-rows-for-merged-cells/)
