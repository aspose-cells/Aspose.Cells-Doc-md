---
title: # GridJsの設定
type: docs
weight: 250
url: /ja/python-net/aspose-cells-gridjs/settings/
description: この記事では、GridJsの設定について説明しています。
keywords: 設定、Excel、ワークブック、GridJs、エディター
---


GridWorkbookSettingsで指定できるいくつかの設定があります :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


たとえば、次のコードはReCalculateOnOpenをfalseに設定して、ファイルを開くときの計算を停止します :
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 次のコードは、ファイルの作成者を設定します :
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
このクラスでさらなる設定を確認できます。

