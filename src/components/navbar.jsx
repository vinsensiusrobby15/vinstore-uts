import React from "react";
import { Link } from "react-router-dom";
import "./navbar.css";
import { Icon } from '@iconify/react';


export const Navbar = () => {
  return (
    <div className="navbar">
      <div className="logo">
        <img src="https://iili.io/JfHO4fe.png" alt="" />
      </div>
      <div className="links">
        <Link to="/"> Beranda </Link>
        <Link to="/contact"> Kontak Kami </Link>
        <Link to="/cart">
          <Icon icon="icon-park-outline:shopping-bag" />
        </Link>
      </div>
    </div>
  );
};
