---
title: ページ設定
type: docs
weight: 80
url: /ja/reportingservices/page-setup/
---

構成には2つのセクションと8種類のページ設定プロパティが含まれています。これらのプロパティには、名前、インデックス、FitToPagesTall、FitToPagesWide、TopMargin、FooterMargin、HeaderMargin、BottomMargin、LeftMargin、RightMarginが含まれています。

- **name**はレポート名を表し、空白の場合はレポート全体を表します。
- **index**はエクスポートされたExcelファイルのワークシートのインデックスを表します。
- **FitToPagesTall**は印刷時にワークシートがスケーリングされる縦のページ数を表します。
- **FitToPagesWide**は印刷時にワークシートがスケーリングされる横のページ数を表します。
- **FooterMargin**はページの下部からフッターまでの距離をセンチメートル単位で表します。
- **HeaderMargin**はページの上部からヘッダーまでの距離をセンチメートル単位で表します。
- **LeftMargin**は左余白のサイズをセンチメートル単位で表します。
- **RightMargin**は右余白のサイズをセンチメートル単位で表します。
- **TopMargin**は上部余白のサイズをセンチメートル単位で表します。
- **BottomMargin**は下部余白のサイズをセンチメートル単位で表します。

ページ設定の構成例

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
