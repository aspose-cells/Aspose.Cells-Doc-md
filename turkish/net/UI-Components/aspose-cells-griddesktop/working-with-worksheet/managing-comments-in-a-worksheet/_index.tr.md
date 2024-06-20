---
title: Çalışma Sayfasında Yorumları Yönetme
type: docs
weight: 110
url: /tr/net/aspose-cells-griddesktop/manage-comments-in-a-worksheet/
keywords: GridDesktop, yorum, yorumlar
description: Bu makale, GridDesktop ta yorumla çalışmayı nasıl tanıtacağınızı açıklar.
---

{{% alert color="primary" %}} 

MS Excel'de, kullanıcıların hücrelere yorum eklemelerine izin veren yorum özelliğini mutlaka biliyor olmalısınız. Bu özellik, kullanıcıların hücrelere değer girmeye hazırlandıklarında kullanıcılara bazı bilgiler sağlamak gerektiğinde faydalıdır. Kullanıcı, yorumlu bir hücreye fare imleci yerleştirdiğinde, kullanıcıya bazı bilgiler sağlamak için küçük bir açılır pencere mesajı belirir. Aspose.Cells.GridDesktop kullanarak, geliştiriciler hücrelere yorum ekleyebilirler. Bu konuda, bu özelliğin kullanımını detaylı olarak açıklayacağız.

{{% /alert %}} 
## **Yorum Ekleme**
Aspose.Cells.GridDesktop kullanarak bir hücreye yorum eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- Yorumun ekleneceği hücreyi (adını veya satır ve sütun numarasını kullanarak) belirterek **Yorum** ekleyin.

Aşağıdaki kod **b2** ve **b4** hücrelerine yorum ekleyecektir.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**Worksheet** nesnesindeki **Comments** koleksiyonu aşırı yükleme **Add** yöntemi sağlar. Geliştiriciler, belirli ihtiyaçlarına göre **Add** yönteminin herhangi bir aşırı yüklü sürümünü kullanabilirler.
## **Yorumlara Erişme**
Çalışma sayfasındaki mevcut bir yoruma erişmek ve değiştirmek isteyen geliştiriciler, yorumu **Comments** koleksiyonundan belirli bir hücreye (hücre adı veya satır ve sütun numarası kullanarak) erişebilirler. Yorum erişildiğinde, geliştiriciler çalışma zamanında metnini değiştirebilirler.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Yorumları Kaldırma**
Mevcut bir yorumu kaldırmak isteyen geliştiriciler, istenen bir çalışma sayfasına erişebilir ve ardından yorumu, yorum içeren hücreyi (adını veya satır ve sütun numarasını kullanarak) **Comments** koleksiyonundan kaldırabilirler.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
