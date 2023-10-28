import React, { useContext } from "react";
import { ShopContext } from "../../context/shop-context";

export const Product = (props) => {
  const { id, itemName, price, itemImage } = props.data;
  const { addToCart, cartItems } = useContext(ShopContext);

  const cartItemCount = cartItems[id];

  return (
    <div className="product">
      <img src={itemImage} alt="" />
      <div className="description">
        <p>
          <b>{itemName}</b>
        </p>
        <p> Rp.{price}</p>
      </div>
      <button className="addToCartBttn" onClick={() => addToCart(id)}>
        Tambahkan Keranjang {cartItemCount > 0 && <> ({cartItemCount})</>}
      </button>
    </div>
  );
};
