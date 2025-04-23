---
title: スプレッドシートエディター  コンポーネント
type: docs
weight: 50
url: /ja/java/spreadsheet-editor-components/
---

**目次**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [WorksheetView](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

HTML5 スプレッドシートエディターは、完全なシステムを構成するためにいくつかのコンポーネントから構成されています。ここではそれぞれの目的と役割を説明します。
### **Index.html**
これは、エディターのUIを説明し、アプリケーションのメインエンドポイントである JSF ページです。Web ブラウザとサーバー間で行われるすべてのインタラクションは、このエンドポイントを介して行われます。

UI の定義に加えて、すべてのバックエンドサービスは、JSF 技術を使用してここにアタッチされます。ユーザーが UI イベントに対話したとき、データはサービスとユーザーの間で行き来し、スプレッドシートのエクスポートなどのタスクを完了します。

これには 2 つの主要な関心事があります。

リボン

上部のタブ付きツールバーエリアをリボンと呼びます。技術的には、それはボタン、ドロップダウン、ラジオメニュー、テキストボックス、およびスプレッドシート上で多くの操作を行うために使用されるいくつかの非表示フィールドを含んでいます。これらのボタンはクリックされると、コマンドがサーバーに送信され、シートがそれに応じて更新されます。

シート

シートは行と列です。セルをクリックすると、それに応じてリボンが更新され、すべてのデータが各セルにアタッチされているため、リクエストをサーバーに送信することなく、リボンが更新されます。リボンはユーザーがシートを移動する際に選択されたセル、行、列を追跡します。

各セルには、そのセルにインラインエディターがあり、セルが編集モードになると表示されます。
### **WorksheetView**
これは、index.html で説明された UI の動的なコンテンツを管理するビュースコープ JSF バックエンドビーンです。ユーザーが UI と対話すると、Ajax リクエストのイベントハンドラを持っています。
### **WorkbookService**
WorkbookService は、ビュースコープの JSF バックエンドビーンです。サービスコンポーネントとして機能し、他のサービスの助けを借りてスプレッドシートをロードおよびアンロードします。次のエンドポイントを持っています。

**init**

**init** は、Java アプリケーションサーバーによってオブジェクトの作成が完了した直後に実行される **PostConstruct** メソッドです。リクエストパラメータマップに **url** パラメータがあるかどうかをチェックし、可能であれば指定された場所から対応するスプレッドシートをロードします。

**destroy**

必要がなくなったリソースをクリーンアップする責任があります。
### **LoaderService**
スプレッドシートのインスタンスを作成し、必要に応じてメモリに保持します。
### **CellsService**
**CellsService** は、行、列、セル、フォーマット、ワークシートの構造のキャッシュを管理します。
{{< app/cells/assistant language="java" >}}
