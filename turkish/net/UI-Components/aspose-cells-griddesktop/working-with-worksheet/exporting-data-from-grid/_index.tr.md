---
title: Grid den Veri Dışa Aktarma
type: docs
weight: 60
url: /tr/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop, veri, dışa aktar, veri dışa aktar
description: Bu makale, GridDesktop ta veri dışa aktarmanın nasıl yapılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Önceki konumuzda Aspose.Cells.GridDesktop kontrolüne bir DataTable'in içeriğini içe aktarmıştık, ancak bilerek Aspose.Cells.GridDesktop'un aynı işlemi desteklediğini belirtmemiştik. Bu nedenle bu konuda, Aspose.Cells.GridDesktop kontrolü içindeki verileri bir DataTable'e nasıl dışa aktarılacağını tartışacağız.

{{% /alert %}} 
## **Grid İçeriğini Dışa Aktarma**
### **Bir Belirli DataTable'e Dışa Aktarma**
Grid içeriğini belirli bir DataTable nesnesine dışa aktarmak için lütfen aşağıdaki adımları izleyin: Aspose.Cells.GridDesktop kontrolünü **Form**'unuza ekleyin.

- İhtiyacınıza göre belirli bir DataTable nesnesi oluşturun.
- Seçilen **Çalışsayfa**'nın verisini belirlediğiniz DataTable nesnesine dışa aktarın.

Aşağıdaki örnekte, içinde dört sütunu olan belirli bir DataTable nesnesi oluşturduk. Son olarak, veri çalışsayfasını (69 satır ve 4 sütun içeren ilk hücreden başlayarak) oluşturduğumuz DataTable nesnesine dışa aktardık.

**Örnek:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Yeni Bir DataTable'e Dışa Aktarma**
Bazı durumlarda, geliştiriciler kendi DataTable nesnelerini oluşturmaktan ziyade sadece çalışsayfa verilerini yeni bir DataTable nesnesine dışa aktarmak isteyebilir. Geliştiriciler için sadece çalışsayfa verilerini hızlı bir şekilde dışa aktarmak daha hızlı olacaktır.

Aşağıdaki örnekte, ExportDataTable yönteminin kullanımını açıklamak için farklı bir yol denedik. Şu anda etkin olan çalışsayfanın referansını aldık ve sonra o etkin çalışsayfanın tüm verisini yeni bir DataTable nesnesine dışa aktardık. Şimdi bu DataTable nesnesi, bir geliştiricinin istediği herhangi bir şekilde kullanılabilir. Örneğin, bir geliştirici bu DataTable nesnesini verileri görmek için bir DataGrid'e bağlayabilir.

**Örnek:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

Yukarıdaki durumda, çalışsayfadan dışa aktarılan verileri içeren yeni bir DataTable nesnesini basitçe geri döndürecek olan ExportDataTable yönteminin aşırı yüklenmiş bir sürümünü kullanacağız.

{{% /alert %}}
