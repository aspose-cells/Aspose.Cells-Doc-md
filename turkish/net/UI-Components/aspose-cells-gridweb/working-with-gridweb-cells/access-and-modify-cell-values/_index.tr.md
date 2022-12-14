---
title: Cell Değerlerine Erişin ve Değiştirin
type: docs
weight: 20
url: /tr/net/access-and-modify-cell-values/
---
{{% alert color="primary" %}} 

[Erişim Çalışma Sayfası Cells](/cells/tr/net/access-worksheet-cells/) hücrelere erişim tartışıldı. Bu konu, bu tartışmayı Aspose.Cells.GridWeb API kullanarak hücre değerlerine nasıl erişileceğini ve değiştirileceğini gösterecek şekilde genişletir.

{{% /alert %}} 
## **Bir Cell Değerine Erişme ve Değiştirme**
### **Dize Değerleri**
 Bir hücreye erişmeden ve hücrenin değerini değiştirmeden önce, hücrelere nasıl erişeceğinizi bilmeniz gerekir. Hücrelere erişim için farklı yaklaşımlar hakkında ayrıntılar için bkz.[Erişim Çalışma Sayfası Cells](/cells/tr/net/access-worksheet-cells/).

Her hücrenin StringValue adlı bir özelliği vardır. Bir hücreye erişildikten sonra geliştiriciler, hücrelerin dize değerine erişmek için StringValue özelliğini kullanabilir. Hücre değerlerini değiştirmek için, hücrenin dize değerini güncellemek için kullanılabilecek özel bir PutValue yöntemi sağlanmıştır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Her Türlü Değer**
Bir hücrenin nesnesinin PutValue yöntemi, bir hücredeki herhangi bir değer türünü (Boolean, int, double, DateTime ve string) değiştirmek için kullanılabilen 8 aşırı yüklemeye sahiptir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



Ayrıca, PutValue yönteminin dize biçimindeki her türlü değeri alıp otomatik olarak uygun bir veri türüne dönüştürebilen aşırı yüklenmiş bir sürümü de vardır. Bunun gerçekleşmesi için aşağıdaki örnekte gösterildiği gibi True Boolean değerini PutValue yönteminin başka bir parametresine iletin.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
