---
title: 更新されたセルだけではなく、ワークシート全体を検証する
type: docs
weight: 80
url: /ja/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
## **考えられる使用シナリオ**
デフォルトでは、GridWeb は更新されたセルのみを検証し、ワークシート全体を検証しません。ただし、GridWeb がリクエストをサーバーに送信する前にクライアント側でワークシート全体を検証する場合は、acwmain.js 内の needValidateall 変数を true に設定する必要があります。
## **更新されたセルだけではなく、ワークシート全体を検証する**
次のスクリーンショットは、acwmain.js の needValidateall 変数を示しています。 true に設定してください。GridWeb は、更新されたセルだけでなく、ワークシート全体を検証します。

![todo:画像_代替_文章](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


