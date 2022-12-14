---
title: Bir Çalışma Sayfasında Cells'e Erişme
type: docs
weight: 10
url: /tr/net/accessing-cells-in-a-worksheet/
---
{{% alert color="primary" %}} 

Şimdiye kadar çalışma sayfaları, satırlar ve sütunlarla çalışmayı tartıştık ama şimdi daha derine inmenin ve hücreler hakkında konuşmanın zamanı geldi. Dolayısıyla, bu konuda, hücreler hakkındaki tartışmamıza hücrelere erişme temel özelliği ile başlayacağız.

{{% /alert %}} 
## **Bir Çalışma Sayfasında Cells'e Erişme**
Aspose.Cells.GridDesktop'un API'ini kullanarak bir çalışma sayfasının herhangi bir hücresine erişebiliriz. Aşağıdaki gibi hücrelere erişmenin üç olası yolu olabilir:

- **Cell Adını Kullanma**
- **Cell'in Satır ve Sütun İndekslerini Kullanma**
- **Odaklanmak Cell**

Yukarıdaki üç yaklaşımı tek tek tartışalım.
### **Cell Adını Kullanma**
 Bir çalışma sayfasındaki tüm hücrelerin benzersiz bir adı vardır. Örneğin, A1, A2, B1, B2 vb. Aspose.Cells.GridDesktop, geliştiricilerin hücre adını kullanarak istenen herhangi bir hücreye erişmelerini sağlar. Tek yapmamız gereken hücre adını (bir dizin olarak)**Cells** koleksiyonu**Çalışma kağıdı**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}
### **Cell'in Satır ve Sütun İndekslerini Kullanma**
 Çalışma sayfasındaki bir hücre, satır ve sütun dizinleri açısından konumu kullanılarak da tanınabilir. Tek yapmamız gereken hücrenin satır ve sütun indislerini hücreye iletmek.**Cells** koleksiyonu**Çalışma kağıdı**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}
### **Odaklanmak Cell**
 Hangi hücreye erişileceğini tam olarak bilmiyorsanız. Ardından Aspose.Cells.GridDesktop, o anda bir kullanıcının odak noktasında bulunan bir hücreye erişmenizi de sağlar. Bu özelliği kullanarak, bir kullanıcının herhangi bir hücreyi seçmesine izin verebilir ve ardından o hücreye arka uçtan erişebilirsiniz. Basitçe kullanılarak elde edilebilir**GetFocusedCell** yöntemi**Çalışma kağıdı**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}
