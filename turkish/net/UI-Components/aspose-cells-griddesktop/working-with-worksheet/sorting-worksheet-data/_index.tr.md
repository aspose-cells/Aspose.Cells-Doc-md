---
title: Çalışma Sayfası Verilerini Sıralama
type: docs
weight: 80
url: /tr/net/aspose-cells-griddesktop/sorting-worksheet-data/
keywords: GridDesktop,sort,sorting,sort data,data sorting
description: Bu makale, GridDesktop taki bir çalışma sayfasında veri sıralamanın nasıl yapılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Sıralama, veri işleme sırasında genellikle kullandığımız önemli bir rutin görevdir. Bu konuda, bir çalışma sayfasında verileri nasıl sıralayabileceğimizi basit bir örnek yardımıyla tartışacağız.

{{% /alert %}} 
## **Çalışma sayfasında verileri sıralamak için Aspose.Cells.GridDesktop API'sını kullanmak için lütfen aşağıdaki adımları izleyin:**
- Önce **CellRange**'in genel bir nesnesini oluşturun, böylece sınıf kapsamında her yerden erişilebilir olabilir

- **GridDesktop**'ın **SelectedCellRangeChanged** olayı için bir olay işleyici oluşturun. **SelectedCellRangeChanged** olayı, bir kullanıcının seçtiği hücre aralığı değiştiğinde her zaman tetiklenir. Örneğin, bir kullanıcı hücreleri (sıralanacak veriler içeren) seçerse, seçim aralığı her değiştiğinde bu olay tetiklenir.
- **GridDesktop**'in **SelectedCellRangeChanged** olayı için olay işleyici oluşturun. **SelectedCellRangeChanged** olayı, bir kullanıcı tarafından seçilen hücre aralığı her değiştirildiğinde tetiklenir. Örneğin, bir kullanıcı (sıralanacak veriler içeren) hücreleri seçerse, her seferinde seçim aralığı değişirse, bu olay tetiklenir.
- Olay işleyicisi, kullanıcı tarafından seçilen hücrelerin güncellenmiş aralığını **CellRange** nesnesi formunda sağlayan **CellRangeEventArgs** argümanını sağlar. Bu olay işleyicisinde, hücrelerin aralığını kaybetmemek için bu **CellRange** nesnesini, diğer kodların da kullanabileceği şekilde, global **CellRange** nesnesine atarız. Hücre aralığını kaybetmemiz gerektiğinden emin olmak için olay işleyici kodunu bir koşul içine yazacağız.
- Şimdi çalışma sayfasına erişmek için bazı kodlar yazabiliriz
- Sıralanacak verileri tutacak bir **SortRange** nesnesi oluşturun. **SortRange** oluşturucuda, sıralanacak çalışma sayfasını, başlangıç ​​satırı ve sütununun endekslerini, sıralanacak satır ve sütun sayısını, sıralamanın yönelimini (örneğin, yukarıdan aşağıya veya soldan sağa) vb. belirtebiliriz.
- Şimdi **SortRange** nesnesinin **Sort** yöntemini çağırarak verilerin sıralamasını yapabiliriz. **Sort** yönteminde, sıralanacak sütun veya satırın endeksini ve sıralama düzenini (gereksinimlerinize göre **Artan** veya **Azalan** olabilir) belirtebiliriz
- Son olarak, hücreleri yeniden çizmek için **GridDesktop**'ın **Invalidate** yöntemini çağırabiliriz.

Aşağıdaki örnekte, bir sütunda veri sıralamanın nasıl yapılacağına dair bir örnek verilmiştir.

Global bir **CellRange** nesnesi oluşturun ve **GridDesktop**'ın **SelectedCellRangeChanged** olayı için bir olay işleyicisi oluşturun. Şimdi aşağıdaki gibi kod yazın:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


**Artan Sıralama** için yöntem yazın. Bir **Artan Sıralama** düğmesi oluşturabilir ve **Click** Olayı içine aşağıdaki gibi kod yazabilirsiniz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


Son olarak, **Azalan Sıralama** işlevselliğini elde etmek için bir **Azalan Sıralama** düğmesi oluşturun ve **Click** Olayı içine aşağıdaki gibi kod yazabilirsiniz.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
