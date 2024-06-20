---
title: Satırların ve Sütunların Otomatik Sığdırması
type: docs
weight: 20
url: /tr/net/autofit-rows-and-columns/
description: Bu makale, Aspose.Cells for .NET API sıyla hücrelerin genişlik ve yüksekliğini içeriğine göre otomatik ayarlama işlemini göstermektedir.
keywords: Satırları otomatik sığdır, sütunları otomatik sığdır, hücre aralığında satırı otomatik sığdır, birleştirilmiş hücrelerin satırlarını otomatik sığdır
---

{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların içeriğine göre hücrelerin genişliğini ve yüksekliğini otomatik ayarlamasına olanak tanır. Bu özellik, Aspose.Cells aracılığıyla da mevcuttur, böylece geliştiriciler hücrelerin boyutlarını çalışma zamanında otomatik ayarlayabilir.

{{% /alert %}}

## **Otomatik Uydurma**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişimi sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bu makale, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfını kullanarak satırları veya sütunları otomatik sığdırma üzerine odaklanmaktadır.

### **Satırı Otomatik Uydurma - Basit**

Bir satırın genişlik ve yüksekliğini otomatik ayarlamak için en doğrudan yaklaşım, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) yöntemini çağırmaktır. [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) yöntemi, yeniden boyutlandırılacak satırın dizinini (satırın dizinini) parametre olarak alır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Hücre Aralığında Satır Otomatik Sığdırma**

Bir satır birçok sütundan oluşur. Aspose.Cells geliştiricilere bir satırın, satır içindeki hücre aralığındaki içeriğe göre otomatik olarak sığdırılmasına olanak tanır. Bunun için [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) yönteminin aşırı yüklenmiş bir sürümü çağrılır. Aşağıdaki parametreleri alır:

- **Satır dizini**, otomatik olarak uyarlama yapılacak satırın dizini.
- **İlk sütun dizini**, satırın ilk sütununun dizini.
- **Son sütun dizini**, satırın son sütununun dizini.

[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) yöntemi, satırın tüm sütunlarının içeriğini kontrol eder ve ardından satırı otomatik olarak sığdırır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Hücre Aralığında Sütun Otomatik Sığdırma**

Bir sütun birçok satırdan oluşur. Bir sütunun, sütun içindeki hücre aralığındaki içeriğe göre otomatik olarak sığdırılması için [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) yönteminin aşırı yüklenmiş bir sürümü çağrılabilir. Aşağıdaki parametreleri alır:

- **Sütun dizini**, otomatik olarak sığdırılacak sütunun dizini.
- **İlk satır indeksi**, sütunun ilk satırının indeksi.
- **Son satır indeksi**, sütunun son satırının indeksi.

[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) metodu sütundaki tüm satırların içeriğini kontrol eder ve ardından sütunu otomatik olarak uygun şekilde ayarlar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Birleştirilmiş Hücreler İçin Satırları Otomatik Uydurma**

Aspose.Cells ile, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API'sını kullanarak birleştirilmiş hücreler için bile satırları otomatik uydurmak mümkündür. [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) sınıfı, birleştirilmiş hücreler için satırları otomatik olarak uydurmak için kullanılabilecek [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) özelliğini sunar. [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) , aşağıdaki üyeleri olan [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) numaralı 'Count' numaralı numaralandırıcıyı kabul eder.

- None: Birleştirilmiş hücreleri görmezden gel.
- FirstLine: Yalnızca ilk satırın yüksekliğini genişletir.
- LastLine: Yalnızca son satırın yüksekliğini genişletir.
- EachLine: Her satırın yüksekliğini genişletir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) ve [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) metotların yüklenmiş versiyonlarını kullanarak, aralık ve seçilen satır/sütunları otomatik olarak uygun şekilde ayarlamak için [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) örneği kullanabilirsiniz.

Yukarıdaki metotların imzaları aşağıdaki gibidir:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) seçenekleri)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) seçenekleri)

{{% /alert %}}

## **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

Bir hücre birleştirildiğinde, AutoFit metotları uygulanmaz, bu da Microsoft Excel'de geçerli olan aynı davranıştır. Bunun üstesinden otomatik filtre API'sini kullanarak gelebilirsiniz. Ayrıca, bir hücredeki metin satır içi bölünmüşse, [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) metodu da uygulanmaz. Bilmeniz gereken başka bir şey de *AutoFit* metotlarının zaman alıcı olmasıdır. Bu nedenle, uygulamanızın verimliliğini sağlamak için bu metotları mümkün olduğunca seyrek çağırmalısınız.

{{% /alert %}}

## **Gelişmiş Konular**
- [Birleştirilmiş Hücreler için Satırları Otomatik Uydurma](/cells/tr/net/autofit-rows-for-merged-cells/)
