---
title: ページ設定
type: docs
weight: 80
url: /ja/reportingservices/page-setup/
---
構成には、2 つのセクションと 8 種類のページ設定プロパティが含まれます。これらのプロパティには、name、index、FitToPagesTall、FitToPagesWide、TopMargin、FooterMargin、HeaderMargin、BottomMargin、LeftMargin、および RightMargin が含まれます。

- **名前**はレポート名を表し、名前が空白の場合はレポート全体を表します。
- **索引**エクスポートされた Excel ファイルのワークシート インデックスを表します。
- **FitToPagesTall**印刷時にワークシートが拡大縮小される高さのページ数を表します。
- **FitToPagesWide**印刷時にワークシートが拡大縮小されるページ幅を表します。
- **フッターマージン**ページの下部からフッターまでの距離をセンチメートル単位で表します。
- **ヘッダーマージン**ページの上部からヘッダーまでの距離をセンチメートル単位で表します。
- **左余白**左マージンのサイズをセンチメートル単位で表します。
- **右余白**右余白のサイズをセンチメートル単位で表します。
- **トップマージン**上余白のサイズをセンチメートル単位で表します。
- **下余白**下余白のサイズをセンチメートル単位で表します。

PageSetup 構成例:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
