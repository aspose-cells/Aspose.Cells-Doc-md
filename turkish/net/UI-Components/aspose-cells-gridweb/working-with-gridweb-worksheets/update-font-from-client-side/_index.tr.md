---
title: Yazı Tipi Ayarlarını İstemci Tarafından Güncelleyin
type: docs
weight: 170
url: /tr/net/update-font-from-client-side/
---
{{% alert color="primary" %}}

Bu konuda, Aspose.Cells.GridWeb denetiminde istemci tarafından yazı tipi ayarlarının değiştirilmesi anlatılmaktadır.

{{% /alert %}}

Aspose.Cells GridWeb artık yazı tipi ayarlarını istemci tarafından değiştirmeyi destekliyor. Bunun için API aşağıdaki işlevleri sağlar

- **updateCellFontStyle**: Parametreler - normal/italik/kalın/italik&&kalın için r/i/b/ib
- **updateCellFontSize**: Parametreler - yazı tipi adı, vb. 'Sistem'
- **updateCellFontName**: Parametreler - yazı tipi boyutu, vb. "12pt"
- **updateCellFontColor**: Parametreler - yok/u/l/ul/ için hiçbiri/altı çizili/üstü çizili/altı çizili&&üstü çizili
- **updateCellFontLine**: Params - #aa22ee gibi html rengi veya yeşil, kırmızı,...
- **updateCellBackGroundColor**: Params - #aa22ee gibi html rengi veya yeşil, kırmızı,...

Aşağıdaki kod parçacığı, GridWeb'de istemci tarafından değişen yazı tipi ayarlarını gösterir.

## Basit kod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-Worksheets-UpdateFontFromClientSide.aspx" >}}
