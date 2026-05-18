from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logger

logger = setup_logger()


class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):
        try:
            logger.info(
                f"Placing order: {symbol} {side} {order_type} Qty={quantity} Price={price}"
            )

            if order_type == "MARKET":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )

            elif order_type == "LIMIT":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            logger.info(f"Order response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise