import typer
from colorama import init, Fore

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

init(autoreset=True)

app = typer.Typer()


@app.command()
def main(
    symbol: str = typer.Argument(...),
    side: str = typer.Argument(...),
    order_type: str = typer.Argument(...),
    quantity: float = typer.Argument(...),
    price: float = typer.Option(None, "--price", "-p")
):
    try:
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        print(Fore.CYAN + "\n========== ORDER REQUEST ==========")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if price:
            print(f"Price       : {price}")

        binance_client = BinanceClient().get_client()

        order_manager = OrderManager(binance_client)

        response = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print(Fore.GREEN + "\n========== ORDER SUCCESS ==========")

        print(f"Order ID       : {response.get('orderId')}")
        print(f"Status         : {response.get('status')}")
        print(f"Executed Qty   : {response.get('executedQty')}")
        print(f"Avg Price      : {response.get('avgPrice')}")

    except Exception as e:
        print(Fore.RED + f"\nERROR: {e}")


if __name__ == "__main__":
    app()