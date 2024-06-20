---
title: GridWeb sayfa değişikliğinde istemci tarafı fonksiyonunu yürütme
type: docs
weight: 70
url: /tr/java/execute-client-side-function-on-gridweb-page-change/
---

## **Olası Kullanım Senaryoları**
Bazen GridWeb sayfa değiştiğinde istemci tarafı fonksiyonunuzu yürütmek isteyebilirsiniz. Aspose.Cells.GridWeb, bunun amacıyla OnPageChangeClientFunction özelliğini sağlar. Lütfen bu özelliği istemci tarafı fonksiyonunuzla ayarlayın bu özelliği yürütmek istediğiniz.
## **GridWeb sayfa değişikliğinde istemci tarafı fonksiyonunu yürütme**
Aşağıdaki java kodu, GridWebBean.setOnPageChangeClientFunction() özelliğin nasıl kullanılacağını anlatır. Bu, özelliği MyOnPageChange adında istemci tarafı işlevi ile ayarlar. Lütfen not edin, bu özellik sadece paging'i etkinleştirdiyseniz geçerlidir, yani GridWebBean.setEnablePaging(true). Şimdi, GridWeb sayfa değiştirdiğinde, **mecra** üzerinde **mevcut sayfa dizinini** yazdıran MyOnPageChange istemci tarafı işlevini çağıracaktır.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Örnek Kod**
Bu, Gridweb.setOnPageChangeClientFunction("MyOnPageChange"); satırından dolayı çalıştırılacak istemci tarafı işlevi MyOnPageChange'in kodudur.

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Aşağıdaki kod, paging'i etkinleştirmeyi ve OnPageChangeClientFunction özelliğini nasıl ayarlayacağını anlatır.

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
