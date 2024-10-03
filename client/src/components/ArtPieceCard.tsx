import React from "react";
import { Link } from "react-router-dom";
import { Card, CardContent } from "@/components/ui/card";
import { ArtPiece } from "../types";

interface ArtPieceCardProps {
  artPiece: ArtPiece;
}

const ArtPieceCard: React.FC<ArtPieceCardProps> = ({ artPiece }) => {
  return (
    <Link to={`/art-piece/${artPiece.id}`}>
      <Card className="h-full">
        <img
          src={artPiece.image_path}
          alt={artPiece.title}
          className="w-full h-48 object-cover"
        />
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold">{artPiece.title}</h3>
          <p className="text-sm text-gray-500">by {artPiece.author.username}</p>
          <p className="text-sm">Rating: {artPiece.global_rating.toFixed(1)}</p>
        </CardContent>
      </Card>
    </Link>
  );
};

export default ArtPieceCard;
