---
title: GridWeb sayfa değişikliğinde istemci tarafı işlevini yürütün
type: docs
weight: 70
url: /tr/java/execute-client-side-function-on-gridweb-page-change/
---
## **Olası Kullanım Senaryoları**
Bazen, GridWeb sayfası değiştiğinde müşteri tarafı işlevinizi yürütmeniz gerekir. Aspose.Cells.GridWeb, bu amaçla OnPageChangeClientFunction özelliğini sağlar. Lütfen bu özelliği, yürütmek istediğiniz istemci tarafı işleviyle ayarlayın.
## **GridWeb sayfa değişikliğinde istemci tarafı işlevini yürütün**
Aşağıdaki java kodu, GridWebBean.setOnPageChangeClientFunction() özelliğinin nasıl kullanılacağını açıklar. Özelliği, MyOnPageChange adlı istemci tarafı işleviyle ayarlar. Lütfen unutmayın, bu özellik yalnızca sayfalamayı etkinleştirdiyseniz geçerlidir, yani GridWebBean.setEnablePaging(true). Şimdi, GridWeb sayfasını ne zaman değiştirirseniz, istemci tarafı işlevi MyOnPageChange'i çağıracaktır.**geçerli sayfa dizini** üzerinde**konsol** bu ekran görüntüsünde gösterildiği gibi.

![yapılacaklar:resim_alternatif_metin](execute-client-side-function-on-gridweb-page-change_1.png)
## **Basit kod**
Bu, bu satır nedeniyle yürütülecek olan istemci tarafı işlevi MyOnPageChange'in kodudur, yani Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Aşağıdaki kod, disk belleğinin nasıl etkinleştirileceğini ve OnPageChangeClientFunction özelliğinin nasıl ayarlanacağını açıklar.

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
