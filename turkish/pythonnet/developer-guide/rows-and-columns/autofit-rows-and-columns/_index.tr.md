---
title: Satırların ve Sütunların Otomatik Sığdırması
type: docs
weight: 20
url: /tr/python-net/autofit-rows-and-columns/
description: Bu makale, Aspose.Cells for Python via .NET API sı ile hücrelerin genişliğini, yüksekliğini, birleştirilmiş hücrelerin satırlarını ve hücre aralığında satırı nasıl otomatik ayarlayacağınızı göstermektedir.
keywords: Python Excel Kütüphanesi, Python Satırları otomatik ayarlama, Python sütunları otomatik ayarlama, Hücre aralığında Python satır otomatik ayarlama, Birleştirilmiş hücrelerin satırlarını otomatik ayarlama.
---

{{% alert color="primary" %}}

Microsoft Excel, hücrelerin genişliğini ve yüksekliğini içeriğine göre otomatik olarak boyutlandırmaya izin verir. Bu özellik, Aspose.Cells for Python via .NET aracılığıyla da mevcuttur, böylece geliştiriciler çalışma zamanında bir hücrenin boyutlarını otomatik olarak ayarlayabilirler.

{{% /alert %}}

## **Otomatik Uydurma**

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bu makale, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfını kullanarak satırları veya sütunları otomatik boyutlandırma üzerinde durmaktadır.

### **Satırı Otomatik Uydurma - Basit**

Bir satırın genişlik ve yüksekliğini otomatik ayarlamak için en doğrudan yaklaşım, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) yöntemini çağırmaktır. [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) yöntemi, yeniden boyutlandırılacak satırın dizinini (satırın dizinini) parametre olarak alır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **Hücre Aralığında Satır Otomatik Sığdırma**

Bir satır birçok sütundan oluşur. Aspose.Cells for Python via .NET, geliştiricilere, satır içindeki hücre aralığındaki içeriğe göre otomatik olarak bir satırı boyutlandırma olanağı sağlar. Bunun için [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) yönteminin yüklenmiş versiyonunu çağırarak aşağıdaki parametreleri alır:

- **Satır dizini**, otomatik olarak uyarlama yapılacak satırın dizini.
- **İlk sütun dizini**, satırın ilk sütununun dizini.
- **Son sütun dizini**, satırın son sütununun dizini.

[**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) yöntemi, satırın tüm sütunlarının içeriğini kontrol eder ve ardından satırı otomatik olarak sığdırır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **Hücre Aralığında Sütun Otomatik Sığdırma**

Bir sütun birçok satırdan oluşur. Bir sütunun, sütun içindeki hücre aralığındaki içeriğe göre otomatik olarak sığdırılması için [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) yönteminin aşırı yüklenmiş bir sürümü çağrılabilir. Aşağıdaki parametreleri alır:

- **Sütun dizini**, otomatik olarak sığdırılacak sütunun dizini.
- **İlk satır indeksi**, sütunun ilk satırının indeksi.
- **Son satır indeksi**, sütunun son satırının indeksi.

[**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) metodu sütundaki tüm satırların içeriğini kontrol eder ve ardından sütunu otomatik olarak uygun şekilde ayarlar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **Birleştirilmiş Hücreler İçin Satırları Otomatik Uydurma**

Aspose.Cells for Python via .NET ile [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) APIsini kullanarak bile birleştirilmiş hücreler için satırları otomatik olarak ayarlamak mümkündür. [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) sınıfı, birleştirilmiş hücreler için satırları otomatik olarak ayarlamak için kullanılabilecek [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) özelliği sağlar. [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) , aşağıdaki üyelere sahip olan [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype) numaralı yenilenebilir değeri kabul eder.

- YOK: Birleştirilmiş hücreleri yok say.
- İLK SATIR: Yalnızca ilk satırın yüksekliğini genişletir.
- SON SATIR: Yalnızca son satırın yüksekliğini genişletir.
- HER SATIR: Yalnızca her satırın yüksekliğini genişletir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

[**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions) ve [**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions) metotların yüklenmiş versiyonlarını kullanarak, aralık ve seçilen satır/sütunları otomatik olarak uygun şekilde ayarlamak için [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) örneği kullanabilirsiniz.

Yukarıdaki metotların imzaları aşağıdaki gibidir:

1. auto_fit_rows(başlangıç_satırı, bitiş_satırı, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) seçenekleri)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

Bir hücre birleştirildiğinde, AutoFit metotları uygulanmaz, bu da Microsoft Excel'de geçerli olan aynı davranıştır. Bunun üstesinden otomatik filtre API'sini kullanarak gelebilirsiniz. Ayrıca, bir hücredeki metin satır içi bölünmüşse, [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) metodu da uygulanmaz. Bilmeniz gereken başka bir şey de *AutoFit* metotlarının zaman alıcı olmasıdır. Bu nedenle, uygulamanızın verimliliğini sağlamak için bu metotları mümkün olduğunca seyrek çağırmalısınız.

{{% /alert %}}

## **Gelişmiş Konular**
- [Birleştirilmiş Hücreler için Satırları Otomatik Uydurma](/cells/tr/python-net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="python-net" >}}
