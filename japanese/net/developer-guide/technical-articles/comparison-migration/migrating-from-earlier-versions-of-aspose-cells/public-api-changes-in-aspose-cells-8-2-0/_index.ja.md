---
title: パブリック API Aspose.Cells 8.2.0 の変更点
type: docs
weight: 70
url: /ja/net/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、バージョン 8.1.2 から 8.2.0 への Aspose.Cells API の変更点について説明します。これは、モジュール/アプリケーション開発者にとって興味深いものです。これには、新規および更新されたパブリック メソッドだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **Cells クラスの MultiThreadReading プロパティを追加**
Aspose.Cells for .NET 8.2.0 では、MultiThreadReading プロパティが Cells クラスに追加され、複数のスレッドでセル値を同時に読み取るためのより堅牢なメカニズムが提供されます。マルチスレッド アプリケーションでブール型プロパティを true に設定すると、各スレッドが正しいセル値を受け取るようになります。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[マルチスレッド環境で Cells 値を同時に読み取る](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously)詳細については。

{{% /alert %}}
## **AutoFitRows および AutoFitColumns メソッドのオーバーロードを追加**
AutoFitRows と AutoFitColumns の新しいオーバーロードが Worksheet クラスに追加され、開発者は AutoFitterOptions クラスのインスタンスを渡しながら、それぞれの範囲に基づいて行と列を自動調整できるようになりました。

前述のメソッドのシグネチャは次のとおりです。

1. AutoFitRows (int startRow、int endRow、AutoFitterOptions オプション)
1. AutoFitColumns (int firstColumn、int lastColumn、AutoFitterOptions オプション)

{{% alert color="primary" %}} 

の詳細記事をご確認ください[行と列の自動調整](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
