---
title: Çalışma Sayfası Verilerini Sıralama
type: docs
weight: 80
url: /tr/net/sorting-worksheet-data/
---
{{% alert color="primary" %}} 

Sıralama, verileri işlerken çoğunlukla kullandığımız önemli bir rutin görevdir. Bu konumuzda, bir çalışma sayfasındaki verileri nasıl sıralayabileceğimizi basit bir örnek yardımıyla tartışacağız.

{{% /alert %}} 
## **Çalışma Sayfası Verilerini Sıralama**
Aspose.Cells.GridDesktop'un API'ini kullanarak bir çalışma sayfasındaki verileri sıralamak için lütfen aşağıdaki adımları izleyin:

-  Her şeyden önce global bir nesne oluşturun**Hücre Aralığı** böylece sınıfınızın kapsamındaki herhangi bir yerden erişilebilir
-  Şunun için bir olay işleyicisi oluşturun:**SeçilenHücre AralığıDeğiştirildi** olayı**IzgaraMasaüstü**. **SeçilenHücre AralığıDeğiştirildi** olay, bir kullanıcı tarafından seçilen bir hücre aralığı her değiştirildiğinde tetiklenir. Örneğin, bir kullanıcı hücreleri (sıralanacak verileri içeren) seçerse, seçim aralığı her değiştiğinde bu olay tetiklenir.
-  Olay işleyici sağlar**CellRangeEventArgs** hücre güncelleme aralığını (kullanıcı tarafından seçilen) ayrıca bir biçimde sağlayan argüman**Hücre Aralığı** nesne. Yani, bu olay işleyicide, bunu atayacağız**Hücre Aralığı** nesne (güncellenmiş hücre aralığını içeren) global**Hücre Aralığı**kodun diğer bölümlerinde de kullanılabilmesi için nesne. Hücre aralığını kaybetmediğimizden emin olmak için bir koşul içine olay işleyici kodu yazacağız.
- Artık çalışma sayfası verilerini sıralamak için bazı kodlar yazabiliriz. Her şeyden önce, istediğiniz bir çalışma sayfasına erişin
-  Oluşturmak**Sıralama Aralığı** verileri sıralanacak olan hücrelerin aralığını tutacak nesne. İçinde**Sıralama Aralığı** yapıcı, çalışma sayfasını, başlangıç satırı ve sütun dizinlerini, sıralanacak satır ve sütun sayısını, sıralama yönünü (yukarıdan aşağıya veya soldan sağa gibi) vb. belirtebiliriz.
-  şimdi arayabiliriz**Çeşit** yöntemi**Sıralama Aralığı** veri sıralamasını gerçekleştirmek için nesne. İçinde**Çeşit** yönteminde, sıralanacak sütun veya satırın dizinini ve sıralama düzenini (bu olabilir**artan** veya**Azalan** gereksinimlerinize göre)
-  Sonunda arayabiliriz**Geçersiz kılmak** yöntemi**IzgaraMasaüstü** hücreleri yeniden çizmek için

Aşağıda verilen örnekte, bir sütundaki verilerin nasıl sıralanacağını gösterdik.

 Global bir CellRange nesnesi oluşturun ve**SeçilenHücre AralığıDeğiştirildi**GridDesktop olayı. Şimdi aşağıdaki gibi kodu yazın:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


 Şimdi için metod yazıyoruz.**Artan Sıralama** . için bir düğme oluşturabilirsiniz.**Artan Sıralama** ve içine aşağıdaki kodu yazın**Tıklamak** Etkinlik.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


 Son olarak, elde etmek için bazı kodlar yazıyoruz.**Azalan Sıralama** işlevsellik. Oluşturmak**Azalan Sıralama** butonuna basın ve içine aşağıdaki kodu yazın.**Tıklamak** Etkinlik.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
