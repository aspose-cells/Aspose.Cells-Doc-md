---
title: Verileri Grid'den Dışa Aktarma
type: docs
weight: 60
url: /tr/net/exporting-data-from-grid/
---
{{% alert color="primary" %}} 

Önceki konumuzda, bir DataTable içeriğini Aspose.Cells.GridDesktop kontrolüne aktarmaktan bahsetmiştik ama Aspose.Cells.GridDesktop'un ters işlemi de desteklediğinden özellikle bahsetmedik. Bu nedenle, bu konuda, Aspose.Cells.GridDesktop denetimi içindeki verileri bir DataTable'a aktarmayı tartışacağız.

{{% /alert %}} 
## **Kılavuz İçeriğini Dışa Aktarma**
### **Belirli bir DataTable'a Aktarma**
 Grid içeriklerini belirli bir DataTable nesnesine aktarmak için lütfen aşağıdaki adımları izleyin: Aspose.Cells.GridDesktop denetimini**Biçim**.

- İhtiyaçlarınıza göre belirli bir DataTable nesnesi oluşturun.
-  Seçilen bir veriyi dışa aktarın**Çalışma kağıdı** belirttiğiniz DataTable nesnesine.

Aşağıda verilen örnekte, içinde dört sütun bulunan belirli bir DataTable nesnesi oluşturduk. Son olarak, çalışma sayfası verilerini (69 satır ve 4 sütunlu ilk hücreden başlayarak) zaten bizim tarafımızdan oluşturulmuş bir DataTable nesnesine aktardık.

**Örnek:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Yeni bir DataTable'a Aktarma**
Bazen, geliştiriciler kendi DataTable nesnelerini oluşturmakla ilgilenmeyebilirler ve çalışma sayfası verilerini yeni bir DataTable nesnesine dışa aktarmak gibi basit bir ihtiyaçları olabilir. Geliştiricilerin yalnızca çalışma sayfası verilerini dışa aktarması daha hızlı bir yol olacaktır.

Aşağıda verilen örnekte, ExportDataTable yönteminin kullanımını farklı bir şekilde açıklamaya çalıştık. Halihazırda aktif olan çalışma sayfasının referansını aldık ve ardından bu aktif çalışma sayfasının tüm verilerini yeni bir DataTable nesnesine aktardık. Artık bu DataTable nesnesi, bir geliştiricinin istediği herhangi bir şekilde kullanılabilir. Bir örnek için, bir geliştirici verileri görüntülemek için bu DataTable nesnesini bir DataGrid'e bağlayabilir.

**Örnek:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

Yukarıdaki durumda, yalnızca çalışma sayfasından dışa aktarılan verileri içeren yeni bir DataTable nesnesi döndürecek olan ExportDataTable yönteminin aşırı yüklenmiş bir sürümünü kullanacağız.

{{% /alert %}}
