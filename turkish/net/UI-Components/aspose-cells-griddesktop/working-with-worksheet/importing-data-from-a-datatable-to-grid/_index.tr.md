---
title: DataTable'dan Grid'e Veri Aktarma
type: docs
weight: 50
url: /tr/net/importing-data-from-a-datatable-to-grid/
---
{{% alert color="primary" %}} 

.NET Çerçevesinin piyasaya sürülmesinden bu yana Microsoft, verileri bir DataTable nesnesi biçiminde çevrimdışı modda depolamak için mükemmel bir yol sağladı. Geliştiricilerin ihtiyaçlarını anlayan Aspose.Cells.GridDesktop, bir veri tablosundan veri almayı da destekler. Bu konuda bunun nasıl yapılacağı anlatılmaktadır.

{{% /alert %}} 
## **Örnek vermek**
Aspose.Cells.GridDesktop kontrolünü kullanarak bir veri tablosunun içeriğini içe aktarmak için:

1. Bir forma Aspose.Cells.GridDesktop denetimi ekleyin.
1. İçe aktarılacak verileri içeren bir DataTable nesnesi oluşturun.
1. İstediğiniz bir çalışma sayfasının referansını alın.
1. Veri tablosu içeriğini çalışma sayfasına alın.
1. Veri tablosunun sütun adlarına göre çalışma sayfasının sütun başlıklarını ayarlayın.
1. İsterseniz sütunların genişliğini ayarlayın/
1. Çalışma sayfasını görüntüleyin.

Aşağıda verilen örnekte, bir DataTable nesnesi oluşturduk ve onu Products adlı bir veritabanı tablosundan getirilen bazı verilerle doldurduk. Son olarak, Aspose.Cells.GridDesktop kullanarak bu DataTable nesnesinden istenen bir çalışma sayfasına veri aktardık.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
