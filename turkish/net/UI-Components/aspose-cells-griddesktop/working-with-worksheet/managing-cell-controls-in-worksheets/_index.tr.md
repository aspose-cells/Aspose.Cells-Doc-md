---
title: Çalışma Sayfalarında Cell Kontrollerini Yönetme
type: docs
weight: 130
url: /tr/net/managing-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

Bu konuda, Aspose.Cells.GridDesktop'un API'ini kullanarak hücre denetimlerini yönetmeyle ilgili bazı önemli kavramlar açıklanmaktadır. Geliştiricinin çalışma sayfalarından hücre kontrollerine nasıl erişebileceğini, değiştirebileceğini ve kaldırabileceğini açıklayacağız. Hadi bir göz atalım.

{{% /alert %}} 
## **Cell Kontrollerine Erişim**
 Çalışma sayfasındaki mevcut bir hücre kontrolüne erişmek ve değiştirmek için geliştiriciler, çalışma sayfasından belirli bir hücre kontrolüne erişebilir.**Kontroller** koleksiyonu**Çalışma kağıdı** hücre kontrolünün görüntülendiği hücreyi belirterek (hücre adını veya satır ve sütun numaraları cinsinden konumunu kullanarak). Bir hücre kontrolüne erişildiğinde, geliştiriciler çalışma zamanında özelliklerini değiştirebilir. Örneğin, aşağıda verilen örnekte, mevcut bir**Onay Kutusu** hücre kontrolü**Çalışma kağıdı** ve Checked özelliğini değiştirdi.

**ÖNEMLİ:** **Kontroller** koleksiyon, biçimindeki her tür hücre denetimini içerir.**Hücre Kontrolü** nesneler. Bu nedenle, belirli bir hücre kontrolü türüne erişmeniz gerekirse, diyelim ki**Onay Kutusu** o zaman şunu yazmanız gerekecek:**Hücre Kontrolü** itiraz etmek**Onay Kutusu** sınıf.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Cell Denetimlerini Kaldırma**
 Mevcut bir hücre denetimini kaldırmak için, geliştiriciler yalnızca istenen bir çalışma sayfasına erişebilir ve ardından**Kaldırmak** gelen hücre kontrolü**Kontroller** koleksiyonu**Çalışma kağıdı** hücre kontrolünü içeren hücreyi (adını veya satır ve sütun numarasını kullanarak) belirterek.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
