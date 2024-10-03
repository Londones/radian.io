import React from "react";
import ArtPieceCard from "./ArtPieceCard";
import { ArtPiece } from "../types";

interface MasonryGridProps {
  artPieces: ArtPiece[];
}

const MasonryGrid: React.FC<MasonryGridProps> = ({ artPieces }) => {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      {artPieces.map((artPiece) => (
        <ArtPieceCard key={artPiece.id} artPiece={artPiece} />
      ))}
    </div>
  );
};

export default MasonryGrid;
